from new_cipher import *


#test pad generation
def test_genPad_len_3() -> None: #length of insert is length of pad
    assert len(generatePad(3)) == 3

def test_genPad_len_0() -> None: #zero gets length 0
    assert len(generatePad(0)) == 0

def test_genPad_len_1000() -> None: # 1000 gets length 1000
    assert len(generatePad(1000)) == 1000

def test_otpad_file_6() -> None: # length of pad is length of pad file
    genPadfile(generatePad(6))
    with open("otpad.txt") as file:
        assert len(file.read()) == 6

def test_otpad_file_54() -> None: # length of pad is length of pad file
    genPadfile(generatePad(54))
    with open("otpad.txt") as file:
        assert len(file.read()) == 54

def test_random_pad() -> None: #two generated pads are not equal, testing randomness
    assert generatePad(15) != generatePad(15)

#test shift

def test_shift_3A() -> None: # regular shift
    assert shift_pos('A', 3) == 'D'

def test_shift_group_3Z() -> None: # Z wraps
    assert shift_pos('Z', 3) == 'C'

def test_shift_group_negZ() -> None: #negative works
    assert shift_pos('Z', -3) == 'W'

def test_shift__punc() -> None: #does not shift non-letters
    assert shift_pos('!', 1) == '!'

def test_shift__3a() -> None: #lowercase
    assert shift_pos('a', 5) == 'f'

def test_otpcipher() -> None: #characters of pad are successfully shifted to ascii integers
    pad = otp_cipher(generatePad(5))
    for i in range(5):
        assert type(pad[i]) == int

#test encipher pad
def test_addPad_same() -> None: # no shift
    assert ''.join(add_pad('aaa', [65,65,65])) == 'aaa'

def test_addPad_diff() -> None: # different shifts
    assert ''.join(add_pad('aaa', [67,70,66])) == 'cfb'

def test_addPad_same_cap() -> None: # no shift
    assert ''.join(add_pad('AAA', [65,65,65])) == 'AAA'

def test_addPad_und() -> None: # different shifts
    assert ''.join(add_pad('AAA', [67,70,66])) == 'CFB'


#test decipher pad

def test_subPad_same() -> None: # no shift
    assert ''.join(sub_pad('aaa', [65,65,65])) == 'aaa'

def test_subPad_diff() -> None: # different shifts
    assert ''.join(sub_pad('cfb', [67,70,66])) == 'aaa'

def test_subPad_same_cap() -> None: # no shift
    assert ''.join(sub_pad('AAA', [65,65,65])) == 'AAA'

def test_subPad_und() -> None: # different shifts
    assert ''.join(sub_pad('CFB', [67,70,66])) == 'AAA'
