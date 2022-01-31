from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import redirect


# Create your views here.
from .models import Photo


def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'photo/list.html', {'photos':photos})


class PhotoUploadView(CreateView):
    model = Photo
    fields = ['photo','text'] #작성장(author), 작성시간(created) 있어야하지만 로그인해서 씀으로 자동처리됨 작성시간도 어떠한 동작때문에 자동으로 됨
    template_name = 'photo/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id # 규칙이다 외워라
        if form.is_valid():
            #데이터가 올바르다면 저장을 하겠다. photo 모델에 인스턴스가 존재하며 저장을하게됨
            form.instance.save()
            return redirect('/') # succes url 이 동작했어야되는게 이거임
        else:
            return self.render_to_response({'form':form})


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'photo/delete.html'


class PhotoUpdateView(UpdateView):
    model = Photo
    fields = ['photo','text']
    template_name = 'photo/update.html'
