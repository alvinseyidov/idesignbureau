from modeltranslation.translator import translator, TranslationOptions
from .models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Category, CategoryTranslationOptions)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(SubCategory, SubCategoryTranslationOptions)


class RoomTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Room, RoomTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Product, ProductTranslationOptions)
