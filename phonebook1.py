
def Pb_read():
      try:
            person = []
            with open('phonebook1.txt', 'r') as f:
                  for line in f.readlines():
                      person.append(line.split(','))
            return person
      except FileNotFoundError:
            with open('phonebook1.txt', 'w+') as f:
                  data = f.readlines()
                  person = data
            return person

def info():
      print('┌──────────────────┐\n'
      '│   주소록 프로그램  │\n'
      '│ 0. 주소록 출력하기 │\n'
      '│ 1. 주소록 입력하기 │\n'
      '│ 2. 주소록 수정하기 │\n'
      '│ 3. 주소록 삭제하기 │\n'
      '│ 4. 주소록 검색하기 │\n'
      '│ 5. 주소록 저장하기 │\n'
      '│ 6. 주소록 불러오기 │\n'
      '│ 7. 주소록 포맷하기 │\n'
      '│ 9. 주소록 종료하기 │\n'
      '└──────────────────┘')

def member_print():
      print('주소록 출력하기를 선택하셨습니다.\n')
      print('입력된 주소록은 아래와 같습니다. \n')
      print('{0:^7}  {1:^2}  {2:^20}'.format('이름', '나이', '주소'))
      for name, age, address in persons:
            print('{0:<5} │ {1:>5} │ {2:<20}'.format(name, age, address.strip()))
      print('\n  * 주소록 출력완료 *\n')

def member_add():
      print('\n주소록 입력하기를 선택하셨습니다.\n'
            '입력하실 이름, 나이, 주소를 적어주세요.')
      name = input(' 이름 : ')
      age = input(' 나이 : ')
      address = input(' 주소 : ')
      persons.append([name, age, address])
      print()
      print('{0:^7}  {1:^2}  {2:^20}'.format('이름', '나이', '주소'))
      for name, age, address in persons:
            print('{0:<5} │ {1:>5} │ {2:<20}'.format(name, age.strip(), address.strip()))
      print('\n  * 주소록 입력완료 *\n')

def member_edit():
      print('주소록 수정하기를 선택하셨습니다.\n')
      edit_name = input('수정할 이름 : ')
      for i in persons:
            if edit_name == i[0]:
                  new_name = input('새로운 이름 : ')
                  new_age = input('새로운 나이 : ')
                  new_addr = input('새로운 주소 : ')

                  i[0] = new_name
                  i[1] = new_age
                  i[2] = new_addr
                  print('\n  * 주소록 수정완료 *\n')
                  break
      else:
            print(' 입력하신 이름을 찾을 수 없습니다.')

def member_del():
      print('주소록 삭제하기를 선택하셨습니다. \n')
      del_name = input('삭제할 이름 : ')
      for i in range(len(persons)):
            if del_name == persons[i][0]:
                  print("\n * 입력한 주소록 :", persons[i][0], persons[i][1], persons[i][2], '*')
                  answer = input('삭제하시겠습니까? (y/n) : ')
                  if answer == 'y':
                        del persons[i]
                        print('\n  * 입력한 주소록 삭제완료 *\n')
                        break
                  else:
                        print('\n * 입력한 주소록 삭제를 취소하셨습니다 * \n')
      else:
            print('\n 입력하신 주소록을 찾을 수 없습니다. \n')

def member_search():
      print('주소록 검색하기를 선택하셨습니다. \n')
      search_name = input('검색할 이름 : ')
      for i in range(len(persons)):
            if search_name == persons[i][0]:
                  print('\n * 검색하신 주소록은 아래와 같습니다. *\n')
                  print('{0:^7}  {1:^2}  {2:^20}'.format('이름', '나이', '주소'))
                  print('{0:<5} │ {1:>3} │ {2:<20}\n'.format(persons[i][0], persons[i][1], persons[i][2]))
                  break
      else:
            print('\n 검색하신 주소록은 없는 주소록입니다.\n')

def member_save():
      with open('phonebook1.txt', 'w+') as f:
            for name, age, address in persons:
                  f.writelines('{0}, {1}, {2}\n'.format(name, age.strip(), address.strip()))
      print('\n   * 입력한 주소록 저장완료 *\n')

def member_read():
      print('주소록 불러오기를 선택하셨습니다. \n')
      print(' * 불러온 주소록은 아래와 같습니다. *')
      print('{0:^7}  {1:^2}  {2:^20}'.format('이름', '나이', '주소'))
      for i in range(len(persons)):
            print('{0:<5} │ {1:>3} │ {2:<20}'.format(persons[i][0], persons[i][1], persons[i][2].strip()))
      print()

def member_format():
      dbcheck = input('정말로 지우시겠습니까? (y/n) ')
      if dbcheck == 'y':
            global persons
            persons = []
            with open('phonebook1.txt', 'w') as f:
                  f.writelines('')
            print('   * 입력한 주소록 포맷완료 *\n')
      else:
            print(' * 포맷하지 않고 메뉴로 돌아갑니다 *\n')
def run():
      menu = 0
      while menu != 9:

            info()
            menu = int(input('원하시는 번호를 입력해주세요. : '))

            if menu == 0:
                  member_print()

            elif menu == 1:
                  member_add()

            elif menu == 2:
                  member_edit()

            elif menu == 3:
                  member_del()

            elif menu == 4:
                  member_search()

            elif menu == 5:
                  member_save()

            elif menu == 6:
                  member_read()

            elif menu == 7:
                  member_format()

            elif menu == 9:
                  print('\n Have a good day ★')
                  exit()

persons = Pb_read()

if __name__ == "__main__":
      run()