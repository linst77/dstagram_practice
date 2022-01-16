from django.shortcuts import render, redirect
from .models import Photo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import UpdateView, DeleteView, DetailView, CreateView
# Create your views here.

@login_required
def photo_list( request):
    # 보여줄 사진 데이터
    print (request.user.id)
    photos = Photo.objects.all()
    # 모든 모델의 오브젝트를 불러온다.
    print (( photos[0].__dict__))

    return render( request, 'photo/list.html', {'photos': photos})
    #args 1) request를 무조건 넣는다, 2) templates의 html 파일 3) photo를 template에 사용할 이름


class PhotoUploadView(LoginRequiredMixin, CreateView):
    model = Photo
    fields = ['photo', 'text'] #작성자( author), 작성시간(create)
    template_name = 'photo/upload.html'
    # html을 통짜로 넣어준다.

    # database에 저장하기 전에 이 데이터가 올바른지 처리
    def form_valid(self, form):
        # author가 꼭 필요하므로 다음과 같이 지정한다.
        form.instance.author_id = self.request.user.id

        if form.is_valid():
            # 데이터가 올바르다면 저장하겠다
            form.instance.save()
            return redirect('/')
        else:
            return self.render_to_response({'form':form})
            # 다시 그 form으로 돌려준다.
            # 회원가입시 패트워드 불일치시 모든 data가 리셋되지 않게 하기 위함

class PhotoDeleteView( LoginRequiredMixin, DeleteView):
    model = Photo
    template_name= 'photo/delete.html'
    success_url = '/'

class PhotoUpdateView( LoginRequiredMixin, UpdateView):
    model = Photo
    template_name= 'photo/update.html'
    fields = ['photo', 'text'] #작성자( author), 작성시간(create)
