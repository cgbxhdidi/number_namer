def main():
    sentence = 'initiate'
    while sentence != '':
        sentence = input("Please type in sentences!\n")
        print(namify_sentence(sentence),'\n')

def name_of_digit(n):
    digit = {0:'zero', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine'}
    return digit[n]

def name_of_tens(n):
    tens = {1:'ten', 2:'twenty', 3:'thirty', 4:'forty', 5:'fifty', 6:'sixty', 7:'seventy', 8:'eighty', 9:'ninety'}
    return tens[n]

def name_of_teens(n):
    teens = {10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen'}
    return teens[n]

def name_of_short_int(n):
    name = []
    n_hun, n_ten_dig = divmod(n, 100)
    if n_hun != 0:
        name.append("%s hundred" % name_of_digit(n_hun))
    if 10 <= n_ten_dig <= 19:
        name.append(name_of_teens(n_ten_dig))
    else:
        n_ten, n_dig = divmod(n_ten_dig, 10)
        if n_ten != 0:
            name.append(name_of_tens(n_ten))
        if n_dig != 0:
            name.append(name_of_digit(n_dig))
    return ' '.join(name)

def name_of_integer(n):
    if n == 0:
        return "zero"
    name = []
    n_mil_tho, n_low = divmod(n, 1000)
    n_mil, n_tho = divmod(n_mil_tho, 1000)
    if n_mil != 0:
        name.append(name_of_short_int(n_mil) + ' million')
    if n_tho != 0:
        name.append(name_of_short_int(n_tho) + ' thousand')
    if n_low != 0:
        name.append(name_of_short_int(n_low))
    return ' '.join(name)

def name_of_fraction(n_tuple):
    if n_tuple[0] == 1:
        name = {10:'tenth', 100:'one hundredth', 1000:'one thousandth'}
        return 'one ' + name[n_tuple[1]]
    name = {10:'tenths', 100:'hundredths', 1000:'thousandths'}
    return name_of_integer(n_tuple[0]) + ' ' + name[n_tuple[1]]

def name_of_decimal(n, n_tuple):
    name = []
    if n != 0:
        name.append(name_of_integer(n))
    if n_tuple[0] != 0:
        name.append(name_of_fraction(n_tuple))
    if name == []:
        return 'zero'
    return ' and '.join(name)
        
def name_in_dollars(dollars, cents):
    name = []
    if dollars != 0 and dollars !=1:
        name.append('%s dollars' % name_of_integer(dollars))
    if dollars == 1:
        name.append('one dollar')
    if cents != 0 and cents !=1:
        name.append('%s cents' % name_of_integer(cents))
    if cents == 1:
        name.append('one cent')
    if name == []:
        return 'zero dollars'
    return ' and '.join(name)

def name_of_number(str_n):
    if '$' in str_n:
        if '.' not in str_n:
            str_n = str_n + '.0'
        money = str_n[1:].split('.')
        return name_in_dollars(int(money[0]), int(money[1]))
    if '.' in str_n:
        x, y = str_n.split('.')
        n = int(x)
        n1, n2 = int(y), int('1'+ '000'[0:len(y)])
        return name_of_decimal(n, (n1, n2))
    return name_of_integer(int(str_n))

def namify_sentence(sentence):
    sentence = '_' + sentence + '_'
    i = 0
    new_sentence = ''
    while i < len(sentence):
        number = ''
        if sentence[i] in '0123456789$':
            while sentence[i] in '0123456789.$':
                number += sentence[i]
                i += 1
            if number[-1] in '$.':
                number = number[:-1]
            if number != '':
                new_sen = (sentence).split(number)
                sentence = name_of_number(number).join(new_sen)
                i = 0
            else:
                i += 1
        else:
            i += 1
    return sentence[1:(len(sentence) - 1)]
    
if __name__ == "__main__":
    main()
