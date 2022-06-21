from django.shortcuts import redirect, render
from .models import Post

# 게시판 앱의 첫화면(원래 로켓화면)
def index(request):
    return render(request, 'board/index.html')

# 게시판 목록(페이지 처리X)
def list(request):
    # Post테이블의 모든 레코드를 id(일련번호:PK)의 내림차순으로 가져온다.
    postlist = Post.objects.all().order_by('-id')
    # 템플릿 렌더링시 컨텍스트 변수 전달
    return render(request, 'board/list.html', {'postlist':postlist})

# 글쓰기 페이지 진입 / 글쓰기 처리
def write(request):
    # 전송방식이 POST라면 submit이므로 폼값을 테이블에 입력한다.
    if request.method=='POST':
        try : 
            Post.objects.create(
                titles=request.POST['titles'],
                contents=request.POST['contents'],
                # 만약 파일첨부를 하지 않으면 여기서 예외가 발생하여
                # except절로 넘어가게된다.
                mainphoto=request.FILES['mainphoto'],
            )
        except :
            # 파일첨부를 하지 않는 경우이므로 제목과 내용만 입력한다.
            Post.objects.create(
                titles=request.POST['titles'],
                contents=request.POST['contents'],
            )
        # 입력 처리가 완료되었다면 리스트로 이동한다.
        return redirect('/board/list/')
    # 전송방식이 POST가 아니라면 글쓰기 페이지 진입을 위해 렌더링한다.
    return render(request, 'board/write.html')

# 글 상세보기
def view(request, pk):
    # 일련번호(PK)에 해당하는 게시물 하나를 select 한다.
    post = Post.objects.get(pk=pk)
    # 가져온 게시물을 컨텍스트 변수로 전달한다.
    return render(request, 'board/view.html', {'post':post})