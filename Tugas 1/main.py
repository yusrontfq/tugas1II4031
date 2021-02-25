import vigenere as vg
import PySimpleGUI as sg
from pathlib import Path

def main():
    sg.theme('BluePurple')
    items = ["Vigenere 26 Key",
             "Vigenere 26 Key - Full",
             "Vigenere 26 Key - Autokey",
             "Extended Vigenere (ASCII)",
             "Playfair"]
    # print("Hasil Enkripsi = ", en)

    layout = [[sg.Text('Masukkan karakter:')],
              [sg.InputText(key='data'), sg.Text('Atau cari file'), sg.FileBrowse(key = 'files')],
              [sg.Text('Masukkan kunci')],
              [sg.InputText(key='kunci')],
              [sg.Text('Jenis cipher')],
              [sg.Combo(items, enable_events=True, key='combo')],
              [sg.Button('Enkripsi'), sg.Button('Dekripsi')]]

    window = sg.Window('Cipher', layout)
    while True:
        event, values = window.read()

        kunci = values['kunci']
        data = values['data']
        if data == '':
            myfile = values['files']
            data = Path(myfile).read_text()

        x = data.upper()
        y = kunci.upper()
        en1 = vg.vig(x,y,'en')
        de1 = vg.vig(x,y,'de')
        en2 = vg.vig_full(x,y,'en')
        de2 = vg.vig_full(x,y,'de')
        en3 = vg.vig_auto(x,y,'en')
        de3 = vg.vig_auto(x,y,'de')
        en4 = vg.vig_ascii(data,kunci,'en')
        de4 = vg.vig_ascii(data,kunci,'de')
        if event is None:
            break
        if event == 'Enkripsi':
            combo = values['combo']
            if combo == 'Vigenere 26 Key':
                sg.Popup("Hasil Enkripsi = ", en1)
            if combo == 'Vigenere 26 Key - Full':
                sg.Popup("Hasil Enkripsi = ", en2)
            if combo == 'Vigenere 26 Key - Autokey':
                sg.Popup("Hasil Enkripsi = ", en3)
            if combo == 'Extended Vigenere (ASCII)':
                sg.Popup("Hasil Enkripsi = ", en4)
        if event == 'Dekripsi':
            combo = values['combo']
            if combo == 'Vigenere 26 Key':
                sg.Popup("Hasil Enkripsi = ", de1)
            if combo == 'Vigenere 26 Key - Full':
                sg.Popup("Hasil Enkripsi = ", de2)
            if combo == 'Vigenere 26 Key - Autokey':
                sg.Popup("Hasil Enkripsi = ", de3)
            if combo == 'Extended Vigenere (ASCII)':
                sg.Popup("Hasil Enkripsi = ", de4)
    window.close()

if __name__ == "__main__":
    main()