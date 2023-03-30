import random
from clear import clear

logo = """                        _..gggggppppp.._                       
                  _.gd$$$$$$$$$$$$$$$$$$bp._                  
               .g$$$$$$P^^""j$$b""  ^^T$$$$$$p.               
            .g$$$P^T$$b    d$P T;       ""^^T$$$p.            
          .d$$P^"  :$; `  :$;                "^T$$b.          
        .d$$P'      T$b.   T$b                  `T$$b.        
       d$$P'      .gg$$$$bpd$$$p.d$bpp.           `T$$b       
      d$$P      .d$$$$$$$$$$$$$$$$$$$$bp.           T$$b      
     d$$P      d$$$$$$$$$$$$$$$$$$$$$$$$$b.          T$$b     
    d$$P      d$$$$$$$$$$$$$$$$$$P^^T$$$$P            T$$b    
   d$$P    '-'T$$$$$$$$$$$$$$$$$$bggpd$$$$b.           T$$b   
  :$$$      .d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p._.g.     $$$;  
  $$$;     d$$$$$$$$$$$$$$$$$$$$$$$P^"^T$$$$P^^T$$$;    :$$$  
 :$$$     :$$$$$$$$$$$$$$:$$$$$$$$$_    "^T$bpd$$$$,     $$$; 
 $$$;     :$$$$$$$$$$$$$$bT$$$$$P^^T$p.    `T$$$$$$;     :$$$ 
:$$$      :$$$$$$$$$$$$$$P `^^^'    "^T$p.    lb`TP       $$$;
:$$$      $$$$$$$$$$$$$$$              `T$$p._;$b         $$$;
$$$;      $$$$$$$$$$$$$$;                `T$$$$:Tb        :$$$
$$$;      $$$$$$$$$$$$$$$                        Tb    _  :$$$
:$$$     d$$$$$$$$$$$$$$$.                        $b.__Tb $$$;
:$$$  .g$$$$$$$$$$$$$$$$$$$p...______...gp._      :$`^^^' $$$;
 $$$;  `^^'T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p.    Tb._, :$$$ 
 :$$$       T$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.   "^"  $$$; 
  $$$;       `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b      :$$$  
  :$$$        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;     $$$;  
   T$$b    _  :$$`$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$;   d$$P   
    T$$b   T$g$$; :$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  d$$P    
     T$$b   `^^'  :$$ "^T$$$$$$$$$$$$$$$$$$$$$$$$$$$ d$$P     
      T$$b        $P     T$$$$$$$$$$$$$$$$$$$$$$$$$;d$$P      
       T$$b.      '       $$$$$$$$$$$$$$$$$$$$$$$$$$$$P       
        `T$$$p.   bug    d$$$$$$$$$$$$$$$$$$$$$$$$$$P'        
          `T$$$$p..__..g$$$$$$$$$$$$$$$$$$$$$$$$$$P'          
            "^$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$^"            
               "^T$$$$$$$$$$$$$$$$$$$$$$$$$$P^"               
                   "^^^T$$$$$$$$$$P^^^ \n
Welcome to the number guessing game!
"""


# generate answer
num_range = range(1, 100, 1)
pick_num = random.choice(num_range)
print(f"(The correct answer is {pick_num}.) \n")

# print(logo)
print(logo)

# generate difficulty
difficulty_correct = False

while not difficulty_correct:
    difficulty = input("Please choose your difficulty: 'easy' or 'hard': ".lower())
    if difficulty == 'easy':
        num_lives = 10
        difficulty_correct = True
    elif difficulty == 'hard':
        num_lives = 5
        difficulty_correct = True
    else:
        print("Invalid answer, please check your spelling and type 'easy' or 'hard' for your difficulty. \n")
clear()
print(f"You have {num_lives} lives. \n")

# guess answer
guess_correct = True

while guess_correct:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess == pick_num:
        clear()
        print(f"You are correct! The answer was {pick_num}.")
        guess_correct = False
    elif guess > pick_num:
        num_lives -= 1
        if num_lives == 0:
            clear()
            print(f"You ran out of turns, the answer was {pick_num}. Game over.")
            guess_correct = False
        else:
            clear()
            print(f"Too high, please try again. You have {num_lives} turns remaining. \n")
    elif guess < pick_num:
        num_lives -= 1
        if num_lives == 0:
            clear()
            print(f"You ran out of turns, the answer was {pick_num}. Game over.")
        else:
            clear()
            print(f"Too low, please try again. You have {num_lives} turns remaining. \n")
