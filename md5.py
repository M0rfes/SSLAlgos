from Crypto.Hash import MD5
h = MD5.new()
plantext = input("Enter a Text")
plantext = bytes(plantext, 'utf-8')
h.update(plantext)
print(f'MD5 Hase for {plantext} is : ', h.hexdigest())
