from modeltranslation.translator import translator, TranslationOptions
from blog.models import Post
from about.models import AboutPost
from portfolio.models import Image


class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class AboutPostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class ImageTranslationOptions(TranslationOptions):
    fields = ('title',)

translator.register(Post, PostTranslationOptions)
translator.register(AboutPost, AboutPostTranslationOptions)
translator.register(Image, ImageTranslationOptions)