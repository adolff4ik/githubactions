from django.test import TestCase
from app import models
from django.contrib.auth.models import User


class PostComment(TestCase):
    def test_post(self):
        author = User.objects.create(username='Stepan Bandera')
        mymodel = models.Post.objects.create(
            author=author,
            title='Hello World!',
            text='Navalniy ne buterbrot s kolbasoy shod ego tudy sudy vizvolat, on v turme i bolshe v blizhayshem, obozrimem budushchem nikogda ne stanet free'
        )
        self.assertEqual(mymodel.author, author)
        self.assertEqual(mymodel.title, 'Hello World!')
        self.assertEqual(mymodel.text, 'Navalniy ne buterbrot s kolbasoy shod ego tudy sudy vizvolat, on v turme i bolshe v blizhayshem, obozrimem budushchem nikogda ne stanet free')

    def test_article(self):
        author = User.objects.create(username='Stepan Bandera')
        mymodel = models.Article.objects.create(
            author=author,
            title='Hello World!',
            text='Navalniy ne buterbrot s kolbasoy shod ego tudy sudy vizvolat, on v turme i bolshe v blizhayshem, obozrimem budushchem nikogda ne stanet free'
        )
        self.assertEqual(mymodel.author, author)
        self.assertEqual(mymodel.title, 'Hello World!')
        self.assertEqual(mymodel.text, 'Navalniy ne buterbrot s kolbasoy shod ego tudy sudy vizvolat, on v turme i bolshe v blizhayshem, obozrimem budushchem nikogda ne stanet free')

    def test_Comment(self):
        author = User.objects.create(username='Stepan Bandera')
        mymodel = models.Comment.objects.create(
            author=author,
            title='Hello World!',
            text='Navalniy ne buterbrot s kolbasoy shod ego tudy sudy vizvolat, on v turme i bolshe v blizhayshem, obozrimem budushchem nikogda ne stanet free'
        )
        self.assertEqual(mymodel.author, author)
        self.assertEqual(mymodel.title, 'Hello World!')
        self.assertEqual(mymodel.text, 'Navalniy ne buterbrot s kolbasoy shod ego tudy sudy vizvolat, on v turme i bolshe v blizhayshem, obozrimem budushchem nikogda ne stanet free')