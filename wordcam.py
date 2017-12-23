
import os,sys,time

def exception():
    print("""
    örnek kullanım 
    
    python3 -r veriniz-veriniz
    veya
    python3 -d veriniz-veriniz
    
    * = boşluktur
    -r = kısa indexleme yap
    -d = tüm verinileri kullanarak indexleme yap
    """)
    quit()


def rastgele(veri):
    try:
        say1 = 0
        say2 = 0
        
        for sayix in veri:
            say1 += 1
        # burada indexleme için bir ön ayar yapılıyo ve hemen aşşagıda mevcut adındaki degişken belirtiliyo
        # bu degişken üzerinde eklem ve çıkarma yapıcagımız bir veri tutmak için oluşturulmuştur
        mevcut = ""
        # aşşagıdaki for döngüsüde artık indexlenmenin kullanıldıgı yerdir.
        source = []
        for say2 in range(say1):
            mevcut = veri[say2]
            q = mevcut + veri[say2 + 1]
            source.append(q + "\n")
            print(q)
            veri[say2 + 2]
    except IndexError:
        print("-----------------------")
        for say2 in range(say1):
            mevcut = veri[say2]
            q1 = str(mevcut) + veri[int("-" + str(say2))]
            say2 -= 1
            print(q1)
            source.append(q1 + "\n")
    except Exception as e:
        print("sorun algılandı !!!!\n", e)

    return source
    print(source)

def dinamik(veri):
    print("dinamik\n")
    source = []
    say1 = 0
    say2 = 0
    for verixx in veri:
        say1 += 1
        
    for dc in veri:
        try:
            for say2 in range(say1):
                sq = dc + veri[say2 + 1]
                source.append(sq + "\n")
                
        except IndexError:
            pass
        
        except Exception as e:
            print("hata mevcut \n sorun algılandı",e)
    return source
    print(source)
try:
    istek = sys.argv[1]
    #istek = request
    veri = sys.argv[2].split("-")

    verix = []
    for i in veri:
        if i == "*":
            veri.append(" ")
        else:
            verix.append(i)

    if istek == "-r" or istek == "-R":
        print("rastgele")
        x = rastgele(verix)
    elif istek == "-d" or istek == "-D":
        print("dinamik")
        x = dinamik(verix)
    else:
        print(None)
        sys.exit()
except Exception as e:
    print(e,"\n\n")
    exception()
# Yapılacak
# bütün sıra dönücek mevcut olan karekter özel bir karaktere eşitlenip listeden çıkarılacak

#print(veri)

try:
    clear_file = open("file.txt", "w")
    clear_file.writelines(x)
    clear_file.__exit__()
except Exception as e:
    print("Program Hata İle Karşılaştı .-!x!-.")
    print(e)
