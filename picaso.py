from PIL import Image

#if the image shows any distortion, keep the size = (500, 500) or toggle with this value to get a perfect image

image = "vegeta.jpg"
output_file = "vegeta.txt"
text = "@PRINCEVEGETA"
size = (1000, 250)
img = Image.open(image).resize(size).convert('L')
pixels, img_size = img.load(), img.size

#creating a file
output = open(output_file,'w')

ct1, ct2 = 0, 0
for i in range(5): output.write('\n\t\t')
for j in range(-2,img_size[1]+2):
    for i in range(-2,img_size[0]+2):
        if i==-2 or j==-2 or i==img_size[0]+1 or j==img_size[1]+1:
            output.write(text[ct2])
            ct2 += 1
            if ct2>len(text)-1: ct2=0
            continue
        elif i==-1 or j==-1 or i==img_size[0] or j==img_size[1]:
            output.write(' ')
            continue
        if pixels[i,j]<64:
            output.write(text[ct1])
            ct1 += 1
            if ct1>len(text)-1: ct1=0
        elif pixels[i,j]<128: output.write('*')
        elif pixels[i,j]<192: output.write('^')
        elif pixels[i,j]<256: output.write('.')
    output.write('\n\t\t')

output.close()
            


