import os

giris = """# espanso configuration file

# This is the default configuration file, change it as you like it
# You can refer to the official documentation:
# https://espanso.org/docs/

# Matches are the substitution rules, when you type the "trigger" string
# it gets replaced by the "replace" string.
matches:
  # Simple text replacement
  - trigger: ":espanso"
    replace: "Hi there!"

  # Dates
  - trigger: ":date"
    replace: "{{mydate}}"
    vars:
      - name: mydate
        type: date
        params:
          format: "%d/%m/%Y"

  # Shell commands
  - trigger: ":shell"
    replace: "{{output}}"
    vars:
      - name: output
        type: shell
        params:
          cmd: "echo Hello from your shell"

#bizimkiler"""

lower_map = {
    ord(u'I'): u'ı',
    ord(u'İ'): u'i',
    ord(u'Ö'): u'ö',
    ord(u'ö'): u'ö',
    ord(u'Ü'): u'ü',
    ord(u'ü'): u'ü',
    ord(u'Ç'): u'ç',
    ord(u'ç'): u'ç',
    ord(u'Ş'): u'ş',
    ord(u'ş'): u'ş',
    ord(u'Ğ'): u'ğ',
    ord(u'ğ'): u'ğ',
    }

ekle ='\n\n  - trigger: ":{}"\n    replace: \"{}"'
biz = "#bizimkiler"
trg = "  - trigger: "
rep = "    replace: "

dr_sil_error_mesage = "Lütfen silmek istediğiniz doktor adını seçiniz!!!"
err_wrong_id = "Lütfen bir doktor ismi seçerek devam edin!!!"
err_wrong_id_kisaltma = "Lütfen bir kısaltma seçerek devam edin!!!"
kisaltma_ekle_error_message = "Lütfen ekleme yapmak istediğiniz doktor adını seçiniz!"
kisaltma_sil_error_message = "Lütfen silmek istediğiniz kısaltmayı seçiniz!"
error_message_baslik_dikkat = "Dikkat!!!"
csmesaj = """Eğer doktoru silerseniz o doktora ait tüm kısaltmalar silinir.
Yine de devam etmek istiyormusun?"""
csbaslik = "Emin Misin?"
csmesajkisaltma = "Bu kısaltmayı silmek istediğinizden emin misiniz?"

dbfile = "db.json"
drdbfile = "drdb.json"
path = os.path.join(os.environ['HOMEPATH'],"AppData","Roaming","espanso")
path_yedek = os.path.join(os.environ['USERPROFILE'],"OneDrive","Masaüstü")
espanso_file = os.path.join(path, "default.yml")
yedekdosya = os.path.join(path_yedek, "default_yedek.yml")
