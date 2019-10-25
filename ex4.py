# Задание 4
# Жду от вас письмо! (слайды 16-20). Воспользуйтесь менеджером контекста (with … as) (слайд 20)
# (Не забудьте для себя понять код из официальной документации – слайд 19).

import smtplib
s = smtplib.SMTP("192.168.0.1", port=25)
s.login('smtp@test.local', '1')
text = str(input("text= "))
s.sendmail(from_addr="smtp@test.local", to_addrs="s.blyznyuk@test.local", msg=text)
s.quit()
