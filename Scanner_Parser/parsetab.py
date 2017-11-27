
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'TRIANGLE DRAW YELLOW WHILE GREEN EIF PRINT CYAN LINE RED STRING BLUE POINT PURPLE ORANGE PINK PLAY SQUARE POLYGON GRAY ELSE FUNC INPUT WHITE CIRCLE RECTANGLE IF AND INT FLOAT BOOL NOT BLACK MAGENTA OR INT_CONST FLOAT_CONST STRING_CONST BOOL_CONST COMMENT BLOCK_COMMENT ASSIGN PLUS_SIGN MINUS_SIGN TIMES_SIGN DIVIDE_SIGN LESS LESS_EQUAL GREATER GREATER_EQUAL EQUAL DIFF PAR_OPEN PAR_CLOSE CURLYB_OPEN CURLYB_CLOSE SQRB_OPEN SQRB_CLOSE COMMA SEMICOLON ID\n    Obi : Play\n    \n    Play : PLAY PAR_OPEN PAR_CLOSE Statements_Block\n    \n    Statements_Block : CURLYB_OPEN Multiple_Statements CURLYB_CLOSE\n    \n    Multiple_Statements : Statement Multiple_Statements\n    | Epsilon\n    \n    Statement : Print\n    \n    Print : PRINT PAR_OPEN Expression PAR_CLOSE SEMICOLON\n    \n    Expression : INT_CONST Save_Int_Const\n    | FLOAT_CONST Save_Float_Const\n    | BOOL_CONST Save_Bool_Const\n    | STRING_CONST Save_String_Const\n    \n    Save_Int_Const :\n    \n    Save_Float_Const :\n    \n    Save_Bool_Const :\n    \n    Save_String_Const :\n    \n    Epsilon :\n    '
    
_lr_action_items = {'PAR_CLOSE':([4,16,17,18,19,20,21,22,23,25,],[5,-12,-14,-13,24,-15,-8,-10,-9,-11,]),'PLAY':([0,],[3,]),'SEMICOLON':([24,],[26,]),'INT_CONST':([14,],[16,]),'BOOL_CONST':([14,],[17,]),'PAR_OPEN':([3,10,],[4,14,]),'FLOAT_CONST':([14,],[18,]),'PRINT':([7,11,12,26,],[10,10,-6,-7,]),'STRING_CONST':([14,],[20,]),'CURLYB_OPEN':([5,],[7,]),'CURLYB_CLOSE':([7,8,9,11,12,15,26,],[-16,13,-5,-16,-6,-4,-7,]),'$end':([1,2,6,13,],[-1,0,-2,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Save_Bool_Const':([17,],[22,]),'Play':([0,],[1,]),'Obi':([0,],[2,]),'Save_Float_Const':([18,],[23,]),'Epsilon':([7,11,],[9,9,]),'Multiple_Statements':([7,11,],[8,15,]),'Statements_Block':([5,],[6,]),'Save_String_Const':([20,],[25,]),'Statement':([7,11,],[11,11,]),'Save_Int_Const':([16,],[21,]),'Print':([7,11,],[12,12,]),'Expression':([14,],[19,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Obi","S'",1,None,None,None),
  ('Obi -> Play','Obi',1,'p_Obi','Parser.py',32),
  ('Play -> PLAY PAR_OPEN PAR_CLOSE Statements_Block','Play',4,'p_Play','Parser.py',37),
  ('Statements_Block -> CURLYB_OPEN Multiple_Statements CURLYB_CLOSE','Statements_Block',3,'p_Statements_Block','Parser.py',42),
  ('Multiple_Statements -> Statement Multiple_Statements','Multiple_Statements',2,'p_Multiple_Statements','Parser.py',48),
  ('Multiple_Statements -> Epsilon','Multiple_Statements',1,'p_Multiple_Statements','Parser.py',49),
  ('Statement -> Print','Statement',1,'p_Statement','Parser.py',55),
  ('Print -> PRINT PAR_OPEN Expression PAR_CLOSE SEMICOLON','Print',5,'p_Print','Parser.py',60),
  ('Expression -> INT_CONST Save_Int_Const','Expression',2,'p_Expression','Parser.py',70),
  ('Expression -> FLOAT_CONST Save_Float_Const','Expression',2,'p_Expression','Parser.py',71),
  ('Expression -> BOOL_CONST Save_Bool_Const','Expression',2,'p_Expression','Parser.py',72),
  ('Expression -> STRING_CONST Save_String_Const','Expression',2,'p_Expression','Parser.py',73),
  ('Save_Int_Const -> <empty>','Save_Int_Const',0,'p_Save_Int_Const','Parser.py',79),
  ('Save_Float_Const -> <empty>','Save_Float_Const',0,'p_Save_Float_Const','Parser.py',91),
  ('Save_Bool_Const -> <empty>','Save_Bool_Const',0,'p_Save_Bool_Const','Parser.py',103),
  ('Save_String_Const -> <empty>','Save_String_Const',0,'p_Save_String_Const','Parser.py',115),
  ('Epsilon -> <empty>','Epsilon',0,'p_Epsilon','Parser.py',128),
]