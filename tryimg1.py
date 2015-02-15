from PIL import Image
import os
from PIL import ImageEnhance
from PIL import ImageFilter


   # Get dimensions
path1 = os.path.abspath(os.path.join("infile"))
path2 = os.path.abspath(os.path.join("outfile"))
print path2
count=0
new_im = Image.new('RGB', (480,480))
for file in os.listdir(path1):
    
    
    count+=1
    current = os.path.join(path1, file)
    
    if os.path.isfile(current):
        if count==1:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (10,10))

        if count==2:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (150,10))

        if count==3:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (300,10))

        if count==4:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (10,150))

        if count==5:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (150,150))

        if count==6:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (300,150))

        if count==7:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (10,300))

        if count==8:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (150,300))

        if count==9:
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                aspect = img.size[1]/120
                new_size = (img.size[0]/aspect, 120)
            else:
                aspect = img.size[0]/120
                new_size = (120, img.size[1]/aspect)
                img.resize(new_size).save(current)
            img = Image.open(current)
            if img.size[0] > img.size[1]:
                new_img = img.crop( ((((img.size[0])-120)/2),  0,120+(((img.size[0])-120)/2),120) )
            else:
                new_img = img.crop( (0,(((img.size[1])-120)/2),120,120+(((img.size[1])-120)/2) ) )

            new_im.paste(new_img, (300,300))


new_im.show()
        
        
        
     


		


