import datetime
import os
import matplotlib.pyplot as plt
import prints

def main(df):

    def filename(extension):
        prints.question('dodać index do zapisanej nazwy?')
        while True:
            x = input('y/n\n')

            if x == 'y':
                i = 1
                while os.path.exists(f'data\EKG{i}_{str(datetime.date.today())}.{extension}'): i += 1
                return f'data\EKG{i}_{str(datetime.date.today())}.{extension}'

            elif x == 'n':
                return f'data\EKG_{str(datetime.date.today())}.{extension}'

            else:
               prints.error('yes or no\n')

    def plot():
        prints.question('chcesz może wykresik?')
        while True:
            x = input('y/n\n')
            if x == 'y':
                prints.message('rysuję Ci wykresik :)')                   
                x = df['t']
                Y = df['V']
                plt.scatter(x, Y, color='b', label='')
                plt.grid()
                plt.xlabel('ms')
                plt.ylabel('V')
                plt.show()
                break

            elif x == 'n':
                prints.message('może innym razem...')
                break
            else:
                prints.error('coś zepsułeś :( spróbuj jeszcze raz')


    # ___________________main__________________________
    prints.question('1 - xlsx\n2 - csv \nmeh - nie zapisuje lol')
    while True:
        name = 0
        x = input('jak chcesz zapisać swoje ekg?\n')
        if x == '1':
            name = filename('xlsx')
            df.to_xlsx(name)
            prints.message(f'zapisano plik pod nazwą <{name}>\n')
            break
        elif x == '2':
            name = filename('csv')
            df.to_csv(name)
            prints.message(f'zapisano plik pod nazwą <{name}>\n')
            break
        elif x == 'meh':
            prints.message('może innym razem...')
            break
        else:
            prints.error('wybierz coś z listy opcji\n')

    plot()
    prints.message('KONIEC')