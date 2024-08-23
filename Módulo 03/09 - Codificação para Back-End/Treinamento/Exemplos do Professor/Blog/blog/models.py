from django.db import models

# funcionalidades como comentários, categorias de postagem.

class Autor(models.Model):
    nome = models.CharField(max_length=50)
    biografia = models.TextField(null=True, blank=True)
    foto_de_perfil = models.CharField(max_length=100, default="models.ImageField(upload_to='fotos_de_perfil/', blank=True, null=True)")
    data_de_registro = models.DateTimeField()

    def __str__(self):
        return self.nome
    

class Tag(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    texto_do_post = models.TextField(null=True, blank=True)
    imagem_do_post = models.CharField(max_length=100, default="models.ImageField(upload_to='imagens_posts/', blank=True, null=True)")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
    
    
class Comentario(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    texto = models.TextField(null=True, blank=True)
    post_referente = models.ForeignKey(Postagem, on_delete=models.CASCADE)

    def __str__(self):
        return "Comentário de " + self.autor.nome
