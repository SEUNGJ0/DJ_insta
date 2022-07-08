from django.shortcuts import render
from django.views import generic
from .models import Photo
from django.shortcuts import redirect
# 함수형 뷰에서 사용하는 권한 제한
from django.contrib.auth.decorators import login_required
# 클레스형 뷰애서 사용하는 권한 제한
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def photo_list(request):
    photos = Photo.objects.all()
    return render(request, 'Dj_Insta_photo/list.html', {'photos':photos})

class PhotoUploadView(LoginRequiredMixin, generic.CreateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'Dj_Insta_photo/upload.html'

    # 업로드 후 이동할 페이지를 호출
    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})

class PhotoDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Photo
    success_url = '/'
    template_name = 'Dj_Insta_photo/delete.html'

class PhotoUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Photo
    fields = ['photo', 'text']
    template_name = 'Dj_Insta_photo/update.html'
