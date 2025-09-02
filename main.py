from keep_alive import keep_alive

# Önce web sunucusunu çalıştır (UptimeRobot bunu ping'leyecek)
keep_alive()

# Sonra botu başlat
import bot  # bot.run() bot.py içinde çağrıldığı için burada import etmek yeterli
