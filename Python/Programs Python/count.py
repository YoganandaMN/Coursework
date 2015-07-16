def main():
          name=raw_input("Enter tha File name")
          handle=open(name,"r")
          text=handle.read()
          word=text.split()
          counts=dict()

          for words in word:
                    counts[words]=counts.get(words,0)+1

          bigcount=None
          bigword=None


          for words,count in counts.items():
                    if bigcount is None or count > bigcount:
                              bigword=words
                              bigcount=count

          print bigword,bigcount



if __name__ == '__main__':
    main()
