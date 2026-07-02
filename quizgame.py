import pgzrun
WIDTH=870
HEIGHT=650
question_box=Rect(20,100,650,150)
answer_box1=Rect(20,300,250,150)
answer_box2=Rect(20,500,250,150)
answer_box3=Rect(300,300,250,150)
answer_box4=Rect(300,500,250,150)
answer_timer=Rect(700,100,150,150)
skipbox=Rect(650,300,150,300)
score=0
time_left=10
is_game_over=False
answer_boxes=[answer_box1,answer_box2,answer_box3,answer_box4]
questions=[]
question_count=0
question_index=0



def draw():
    screen.fill(color="yellow3")
    screen.draw.filled_rect(question_box,"SteelBlue4")
    screen.draw.filled_rect(answer_box1,"LemonChiffon1")
    screen.draw.filled_rect(answer_box2,"LemonChiffon1")
    screen.draw.filled_rect(answer_box3,"LemonChiffon1")
    screen.draw.filled_rect(answer_box4,"LemonChiffon1")
    screen.draw.filled_rect(answer_timer,"tan4")
    screen.draw.filled_rect(skipbox,"OrangeRed4")
    screen.draw.textbox(question[0].strip(), question_box,color="red")
    screen.draw.textbox("skip",skipbox,color="blue")
    screen.draw.textbox(str(time_left),answer_timer,color="white")
    index=1
    for answer_box in answer_boxes:
        screen.draw.textbox(question[index].strip(),answer_box,color="magenta1")
        index+=1

def read_question_file():
    global question_count,questions
    q_file=open("myquestions.txt","r")
    for question in q_file:
        questions.append(question)
        question_count=question_count+1
def read_next_question():
    global question_index
    question_index=question_index+1
    return questions.pop(0).split(",")        

def on_mouse_down(pos):
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
           if index is int (question[5]):
        
              correct_answer()
           else:
               game_over()
        index=index+1  
    if skipbox.collidepoint(pos):
        skip_question()     
        
def correct_answer():
    global score,question,time_left,questions
    score+=1
    if questions:
        question=read_next_question()
        time_left=10
    else:
        game_over()
def game_over():
    global question,time_left,is_game_over
    message="you got"+str(score)+"question correct out of 8"
    question= [message,"you got",str(score),"corect","answer",5]
    time_left=0
    is_game_over=True 
def skip_question():
    global question,time_left
    if questions and not is_game_over:
        question=read_next_question()
        time_left=10
    else:
        game_over() 
def update_time_left():
    global time_left
    if time_left:
      time_left=time_left-1
    else:
        game_over()

     
read_question_file()
question=read_next_question()
clock.schedule_interval(update_time_left,1)
pgzrun.go() 