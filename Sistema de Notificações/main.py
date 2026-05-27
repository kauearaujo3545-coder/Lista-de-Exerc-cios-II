from central_notificacoes import CentralNotificacoes
from notificador_email import NotificadorEmail
from notificador_sms import NotificadorSMS
from notificador_app import NotificadorApp


central = CentralNotificacoes()

email = NotificadorEmail()
sms = NotificadorSMS()
app = NotificadorApp()

central.adicionar_notificador(email)
central.adicionar_notificador(sms)
central.adicionar_notificador(app)

central.enviar_para_todos("Sistema em manutenção às 22h.")
