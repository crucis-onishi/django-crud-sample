from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # インポート
from django.core.exceptions import PermissionDenied # インポート

class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'

class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'

class CreateView(LoginRequiredMixin, generic.edit.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content'] # 項目をcontentのみに変更

    #格納する値をチェック
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = ['content'] # 項目をcontentのみに変更

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied('編集権限がありません。')
        return super(UpdateView, self).dispatch(request, *args, **kwargs)

class DeleteView(LoginRequiredMixin, generic.edit.DeleteView): # 継承
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')
