from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Story, Comment

class StoryListView(ListView):
    model = Story
    template_name = 'home.html'
    context_object_name = 'stories'

    def get_context_data(self, **kwargs):
        context = super(StoryListView, self).get_context_data(**kwargs)
        context['recents'] = Story.objects.order_by('-date')[:2]
        return context

class StoryDetailView(DetailView):
    model = Story
    template_name = 'story_detail.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        context['recents'] = Story.objects.order_by('-date')[:2]
        return context
    
    def post(self, request, *args, **kwargs):
        comment = request.POST['comment']
        self.object = self.get_object()
        new_comment = Comment.objects.create(
            story=self.object,
            comment=comment,
            commenter=self.request.user,
        )
        new_comment.save()
        context = super(StoryDetailView, self).get_context_data(**kwargs)
        context['recents'] = Story.objects.order_by('-date')[:2]
        return self.render_to_response(context=context)


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    template_name = 'story_new.html'
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.writer = self.request.user
        return super().form_valid(form)

class StoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Story
    fields = ('title', 'body',)
    template_name = 'story_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.writer == self.request.user

class StoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Story
    template_name = 'story_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        obj = self.get_object()
        return obj.writer == self.request.user