from video import Video
from podcast import Podcast
from texto_narrado import TextoNarrado
from plataforma import Plataforma


plataforma = Plataforma("EducaTech")

video = Video("Python POO", "15 min", "1080p")
podcast = Podcast("TechCast", "40 min", "João Silva")
texto = TextoNarrado("Introdução à IA", "10 min", "Português")

plataforma.adicionar_midia(video)
plataforma.adicionar_midia(podcast)
plataforma.adicionar_midia(texto)

plataforma.listar_midias()
plataforma.reproduzir_todas()
