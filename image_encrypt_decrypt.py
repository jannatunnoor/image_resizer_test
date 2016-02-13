__author__ = 'jnoor'

import PIL
from PIL import Image
import cStringIO
from Crypto.Cipher import AES
import binascii


def time_test_jpeg():
    """ this is time_tests """
    DIMENSION = 300
    #_obj = 'images_1400_3.jpg'
    obj = 'images_1400_4.png'
    in_file = open(obj,"rb")
    ori_request_body = in_file.read()
    request_body = ori_request_body
    print type(request_body)

    case = 0
    while case<1:
        img = request_body
        try:
            Image.open(cStringIO.StringIO(img))
        except:
            print 'can not open image file error'
            break

        im = Image.open(cStringIO.StringIO(img))
        new_width = new_height = DIMENSION
        print type(im)

        if im.size[0] <= new_width and im.size[1] <= new_height:
            upload_image = img

        else:
            if im.size[0] <= im.size[1]:
                h_percent = (new_height /float(im.size[1]))
                new_width = int((float(im.size[0]) * float(h_percent)))

            else:
                w_percent = ( new_width / float(im.size[0]))
                new_height = int((float(im.size[1]) * float(w_percent)))

            resize_image = cStringIO.StringIO()
            out = im.resize((new_width, new_height), PIL.Image.ANTIALIAS)
            out.save(resize_image, 'JPEG')
            print type(resize_image)
            upload_image = resize_image.getvalue()
            print type(upload_image)

            key = 'mysecretpassword'
            plaintext = upload_image
            #encobj = AES.new(key, AES.MODE_ECB)
            #ciphertext = encobj.encrypt(plaintext)
            ciphertext = 'abcd'
            encryptValue = ciphertext.encode('hex')
            print encryptValue



            ciphertext = binascii.unhexlify(encryptValue)
            #decobj = AES.new(key, AES.MODE_ECB)
            #plaintext = decobj.decrypt(ciphertext)
            plaintext = ciphertext ^ 'abcd'
            print plaintext


        new_obj = str(DIMENSION) + obj.replace(obj.split('.')[-1], 'jpg')
        out_file = open(new_obj, "wb") # open for [w]riting as [b]inary
        out_file.write(upload_image)
        out_file.close()

        case += 1
        request_body = ori_request_body




if __name__ == '__main__':
    import timeit
    print(timeit.timeit("time_test_jpeg()", setup="from __main__ import time_test_jpeg", number = 1))

    #time_test()
    #print 'finish time_test'