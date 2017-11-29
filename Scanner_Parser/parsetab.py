
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'TRIANGLE DRAW YELLOW WHILE GREEN EIF PRINT CYAN LINE RED STRING BLUE POINT PURPLE ORANGE PINK PLAY SQUARE POLYGON GRAY ELSE FUNC INPUT WHITE CIRCLE RECTANGLE IF AND INT FLOAT BOOL NOT BLACK MAGENTA OR INT_CONST FLOAT_CONST STRING_CONST BOOL_CONST COMMENT BLOCK_COMMENT ASSIGN PLUS_SIGN MINUS_SIGN TIMES_SIGN DIVIDE_SIGN MOD_SIGN LESS LESS_EQUAL GREATER GREATER_EQUAL EQUAL DIFF PAR_OPEN PAR_CLOSE CURLYB_OPEN CURLYB_CLOSE SQRB_OPEN SQRB_CLOSE COMMA SEMICOLON ID\n    Obi : Play\n    \n    Play : PLAY Play_Init PAR_OPEN PAR_CLOSE Statements_Block\n    \n    Play_Init :\n    \n    Statements_Block : CURLYB_OPEN Multiple_Statements CURLYB_CLOSE\n    \n    Multiple_Statements : Statement Multiple_Statements\n    | Epsilon\n    \n    Statement : Print\n    \n    Print : PRINT PAR_OPEN Logical_Or PAR_CLOSE SEMICOLON\n    \n    Logical_Or : Logical_And Or_Quad Multiple_Ands\n    \n    Multiple_Ands : OR Push_Or Logical_And Or_Quad Multiple_Ands\n    | Epsilon\n    \n    Or_Quad :\n    \n    Push_Or :\n    \n    Logical_And : Logical_Not And_Quad Multiple_Nots\n    \n    Multiple_Nots : AND Push_And Logical_Not And_Quad Multiple_Nots\n    | Epsilon\n    \n    And_Quad :\n    \n    Push_And :\n    \n    Logical_Not : Relational\n    | NOT Push_Not Relational Not_Quad\n    \n    Not_Quad :\n    \n    Push_Not :\n    \n    Relational : Expression\n    | Expression LESS Push_Less Expression Relational_Quad\n    | Expression LESS_EQUAL Push_Less_Equal Expression Relational_Quad\n    | Expression GREATER Push_Greater Expression Relational_Quad\n    | Expression GREATER_EQUAL Push_Greater_Equal Expression Relational_Quad\n    \n    Relational_Quad :\n    \n    Push_Less :\n    \n    Push_Less_Equal :\n    \n    Push_Greater :\n    \n    Push_Greater_Equal :\n    \n    Expression : Term Sum_Sub_Quad Multiple_Terms\n    \n    Multiple_Terms : PLUS_SIGN Push_Plus_Sign Term Sum_Sub_Quad Multiple_Terms\n    | MINUS_SIGN Push_Minus_Sign Term Sum_Sub_Quad Multiple_Terms\n    | Epsilon\n    \n    Sum_Sub_Quad :\n    \n    Push_Plus_Sign :\n    \n    Push_Minus_Sign :\n    \n    Term : Factor Mult_Div_Mod_Quad Multiple_Factors\n    \n    Multiple_Factors : TIMES_SIGN Push_Times_Sign Factor Mult_Div_Mod_Quad Multiple_Factors\n    | DIVIDE_SIGN Push_Divide_Sign Factor Mult_Div_Mod_Quad Multiple_Factors\n    | MOD_SIGN Push_Mod_Sign Factor Mult_Div_Mod_Quad Multiple_Factors\n    | Epsilon\n    \n    Mult_Div_Mod_Quad :\n    \n    Push_Times_Sign :\n    \n    Push_Divide_Sign :\n    \n    Push_Mod_Sign :\n    \n    Factor : PAR_OPEN Push_False_Bottom Logical_Or PAR_CLOSE Pop_False_Bottom\n    | Var_Cte\n    \n    Push_False_Bottom :\n    \n    Pop_False_Bottom :\n    \n    Var_Cte : INT_CONST Save_Int_Const\n    | MINUS_SIGN INT_CONST Save_Neg_Int_Const\n    | FLOAT_CONST Save_Float_Const\n    | MINUS_SIGN FLOAT_CONST Save_Neg_Float_Const\n    | BOOL_CONST Save_Bool_Const\n    | STRING_CONST Save_String_Const\n    \n    Save_Int_Const :\n    \n    Save_Neg_Int_Const :\n    \n    Save_Float_Const :\n    \n    Save_Neg_Float_Const :\n    \n    Save_Bool_Const :\n    \n    Save_String_Const :\n    \n    Epsilon :\n    '
    
_lr_action_items = {'TIMES_SIGN':([18,19,21,22,24,26,33,34,35,36,38,46,47,70,71,73,86,87,88,89,98,99,100,],[-61,-45,-64,-59,-63,-50,-55,50,-58,-53,-57,-60,-62,-54,-56,-52,-49,-45,-45,-45,50,50,50,]),'PAR_CLOSE':([5,18,19,20,21,22,23,24,25,26,27,28,29,33,34,35,36,37,38,39,41,46,47,49,52,53,56,57,58,59,63,64,70,71,72,73,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,],[6,-61,-45,-19,-64,-59,-17,-63,-37,-50,40,-12,-23,-55,-65,-58,-53,-65,-57,-65,-65,-60,-62,73,-44,-40,-16,-14,-33,-36,-9,-11,-54,-56,-21,-52,-28,-28,-28,-28,-20,-49,-45,-45,-45,-17,-37,-37,-12,-24,-25,-27,-26,-65,-65,-65,-65,-65,-65,-65,-41,-43,-42,-15,-35,-34,-10,]),'LESS':([18,19,21,22,24,25,26,29,33,34,35,36,38,39,46,47,52,53,58,59,70,71,73,86,87,88,89,91,92,98,99,100,102,103,105,106,107,109,110,],[-61,-45,-64,-59,-63,-37,-50,42,-55,-65,-58,-53,-57,-65,-60,-62,-44,-40,-33,-36,-54,-56,-52,-49,-45,-45,-45,-37,-37,-65,-65,-65,-65,-65,-41,-43,-42,-35,-34,]),'PAR_OPEN':([3,4,11,15,17,31,32,42,43,44,45,48,50,51,54,55,60,61,65,66,67,68,69,74,75,76,77,78,79,80,],[-3,5,15,17,-51,-22,17,-29,-30,-32,-31,17,-46,-48,-47,-18,-39,-38,-13,17,17,17,17,17,17,17,17,17,17,17,]),'FLOAT_CONST':([15,17,30,31,32,42,43,44,45,48,50,51,54,55,60,61,65,66,67,68,69,74,75,76,77,78,79,80,],[18,-51,47,-22,18,-29,-30,-32,-31,18,-46,-48,-47,-18,-39,-38,-13,18,18,18,18,18,18,18,18,18,18,18,]),'PRINT':([8,12,13,62,],[11,11,-7,-8,]),'PLUS_SIGN':([18,19,21,22,24,25,26,33,34,35,36,38,39,46,47,52,53,70,71,73,86,87,88,89,91,92,98,99,100,102,103,105,106,107,],[-61,-45,-64,-59,-63,-37,-50,-55,-65,-58,-53,-57,61,-60,-62,-44,-40,-54,-56,-52,-49,-45,-45,-45,-37,-37,-65,-65,-65,61,61,-41,-43,-42,]),'STRING_CONST':([15,17,31,32,42,43,44,45,48,50,51,54,55,60,61,65,66,67,68,69,74,75,76,77,78,79,80,],[21,-51,-22,21,-29,-30,-32,-31,21,-46,-48,-47,-18,-39,-38,-13,21,21,21,21,21,21,21,21,21,21,21,]),'INT_CONST':([15,17,30,31,32,42,43,44,45,48,50,51,54,55,60,61,65,66,67,68,69,74,75,76,77,78,79,80,],[22,-51,46,-22,22,-29,-30,-32,-31,22,-46,-48,-47,-18,-39,-38,-13,22,22,22,22,22,22,22,22,22,22,22,]),'SEMICOLON':([40,],[62,]),'GREATER_EQUAL':([18,19,21,22,24,25,26,29,33,34,35,36,38,39,46,47,52,53,58,59,70,71,73,86,87,88,89,91,92,98,99,100,102,103,105,106,107,109,110,],[-61,-45,-64,-59,-63,-37,-50,44,-55,-65,-58,-53,-57,-65,-60,-62,-44,-40,-33,-36,-54,-56,-52,-49,-45,-45,-45,-37,-37,-65,-65,-65,-65,-65,-41,-43,-42,-35,-34,]),'MOD_SIGN':([18,19,21,22,24,26,33,34,35,36,38,46,47,70,71,73,86,87,88,89,98,99,100,],[-61,-45,-64,-59,-63,-50,-55,51,-58,-53,-57,-60,-62,-54,-56,-52,-49,-45,-45,-45,51,51,51,]),'BOOL_CONST':([15,17,31,32,42,43,44,45,48,50,51,54,55,60,61,65,66,67,68,69,74,75,76,77,78,79,80,],[24,-51,-22,24,-29,-30,-32,-31,24,-46,-48,-47,-18,-39,-38,-13,24,24,24,24,24,24,24,24,24,24,24,]),'$end':([1,2,7,14,],[-1,0,-2,-4,]),'PLAY':([0,],[3,]),'LESS_EQUAL':([18,19,21,22,24,25,26,29,33,34,35,36,38,39,46,47,52,53,58,59,70,71,73,86,87,88,89,91,92,98,99,100,102,103,105,106,107,109,110,],[-61,-45,-64,-59,-63,-37,-50,43,-55,-65,-58,-53,-57,-65,-60,-62,-44,-40,-33,-36,-54,-56,-52,-49,-45,-45,-45,-37,-37,-65,-65,-65,-65,-65,-41,-43,-42,-35,-34,]),'AND':([18,19,20,21,22,23,24,25,26,29,33,34,35,36,37,38,39,46,47,52,53,58,59,70,71,72,73,81,82,83,84,85,86,87,88,89,90,91,92,94,95,96,97,98,99,100,101,102,103,105,106,107,109,110,],[-61,-45,-19,-64,-59,-17,-63,-37,-50,-23,-55,-65,-58,-53,55,-57,-65,-60,-62,-44,-40,-33,-36,-54,-56,-21,-52,-28,-28,-28,-28,-20,-49,-45,-45,-45,-17,-37,-37,-24,-25,-27,-26,-65,-65,-65,55,-65,-65,-41,-43,-42,-35,-34,]),'GREATER':([18,19,21,22,24,25,26,29,33,34,35,36,38,39,46,47,52,53,58,59,70,71,73,86,87,88,89,91,92,98,99,100,102,103,105,106,107,109,110,],[-61,-45,-64,-59,-63,-37,-50,45,-55,-65,-58,-53,-57,-65,-60,-62,-44,-40,-33,-36,-54,-56,-52,-49,-45,-45,-45,-37,-37,-65,-65,-65,-65,-65,-41,-43,-42,-35,-34,]),'CURLYB_OPEN':([6,],[8,]),'DIVIDE_SIGN':([18,19,21,22,24,26,33,34,35,36,38,46,47,70,71,73,86,87,88,89,98,99,100,],[-61,-45,-64,-59,-63,-50,-55,54,-58,-53,-57,-60,-62,-54,-56,-52,-49,-45,-45,-45,54,54,54,]),'MINUS_SIGN':([15,17,18,19,21,22,24,25,26,31,32,33,34,35,36,38,39,42,43,44,45,46,47,48,50,51,52,53,54,55,60,61,65,66,67,68,69,70,71,73,74,75,76,77,78,79,80,86,87,88,89,91,92,98,99,100,102,103,105,106,107,],[30,-51,-61,-45,-64,-59,-63,-37,-50,-22,30,-55,-65,-58,-53,-57,60,-29,-30,-32,-31,-60,-62,30,-46,-48,-44,-40,-47,-18,-39,-38,-13,30,30,30,30,-54,-56,-52,30,30,30,30,30,30,30,-49,-45,-45,-45,-37,-37,-65,-65,-65,60,60,-41,-43,-42,]),'NOT':([15,17,32,55,65,77,80,],[31,-51,31,-18,-13,31,31,]),'OR':([18,19,20,21,22,23,24,25,26,28,29,33,34,35,36,37,38,39,41,46,47,52,53,56,57,58,59,70,71,72,73,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,],[-61,-45,-19,-64,-59,-17,-63,-37,-50,-12,-23,-55,-65,-58,-53,-65,-57,-65,65,-60,-62,-44,-40,-16,-14,-33,-36,-54,-56,-21,-52,-28,-28,-28,-28,-20,-49,-45,-45,-45,-17,-37,-37,-12,-24,-25,-27,-26,-65,-65,-65,-65,-65,-65,65,-41,-43,-42,-15,-35,-34,]),'CURLYB_CLOSE':([8,9,10,12,13,16,62,],[-65,14,-6,-65,-7,-5,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Push_Minus_Sign':([60,],[78,]),'Push_Greater':([45,],[69,]),'Multiple_Ands':([41,104,],[63,111,]),'Push_Less_Equal':([43,],[67,]),'Not_Quad':([72,],[85,]),'Push_Greater_Equal':([44,],[68,]),'Term':([15,32,48,66,67,68,69,77,78,79,80,],[25,25,25,25,25,25,25,25,91,92,25,]),'Multiple_Nots':([37,101,],[57,108,]),'Statement':([8,12,],[12,12,]),'Factor':([15,32,48,66,67,68,69,74,75,76,77,78,79,80,],[19,19,19,19,19,19,19,87,88,89,19,19,19,19,]),'Print':([8,12,],[13,13,]),'Relational':([15,32,48,77,80,],[20,20,72,20,20,]),'Mult_Div_Mod_Quad':([19,87,88,89,],[34,98,99,100,]),'Sum_Sub_Quad':([25,91,92,],[39,102,103,]),'Or_Quad':([28,93,],[41,104,]),'Play':([0,],[1,]),'Logical_Not':([15,32,77,80,],[23,23,90,23,]),'Push_And':([55,],[77,]),'Save_String_Const':([21,],[35,]),'Epsilon':([8,12,34,37,39,41,98,99,100,101,102,103,104,],[10,10,52,56,59,64,52,52,52,56,59,59,64,]),'Push_Times_Sign':([50,],[74,]),'Push_Mod_Sign':([51,],[75,]),'Multiple_Factors':([34,98,99,100,],[53,105,106,107,]),'Push_Or':([65,],[80,]),'Save_Bool_Const':([24,],[38,]),'Multiple_Statements':([8,12,],[9,16,]),'And_Quad':([23,90,],[37,101,]),'Push_Less':([42,],[66,]),'Obi':([0,],[2,]),'Save_Float_Const':([18,],[33,]),'Pop_False_Bottom':([73,],[86,]),'Var_Cte':([15,32,48,66,67,68,69,74,75,76,77,78,79,80,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'Logical_Or':([15,32,],[27,49,]),'Play_Init':([3,],[4,]),'Logical_And':([15,32,80,],[28,28,93,]),'Push_Not':([31,],[48,]),'Expression':([15,32,48,66,67,68,69,77,80,],[29,29,29,81,82,83,84,29,29,]),'Save_Neg_Int_Const':([46,],[70,]),'Multiple_Terms':([39,102,103,],[58,109,110,]),'Save_Neg_Float_Const':([47,],[71,]),'Statements_Block':([6,],[7,]),'Push_Plus_Sign':([61,],[79,]),'Relational_Quad':([81,82,83,84,],[94,95,96,97,]),'Save_Int_Const':([22,],[36,]),'Push_Divide_Sign':([54,],[76,]),'Push_False_Bottom':([17,],[32,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Obi","S'",1,None,None,None),
  ('Obi -> Play','Obi',1,'p_Obi','Parser.py',54),
  ('Play -> PLAY Play_Init PAR_OPEN PAR_CLOSE Statements_Block','Play',5,'p_Play','Parser.py',60),
  ('Play_Init -> <empty>','Play_Init',0,'p_Play_Init','Parser.py',65),
  ('Statements_Block -> CURLYB_OPEN Multiple_Statements CURLYB_CLOSE','Statements_Block',3,'p_Statements_Block','Parser.py',75),
  ('Multiple_Statements -> Statement Multiple_Statements','Multiple_Statements',2,'p_Multiple_Statements','Parser.py',81),
  ('Multiple_Statements -> Epsilon','Multiple_Statements',1,'p_Multiple_Statements','Parser.py',82),
  ('Statement -> Print','Statement',1,'p_Statement','Parser.py',88),
  ('Print -> PRINT PAR_OPEN Logical_Or PAR_CLOSE SEMICOLON','Print',5,'p_Print','Parser.py',93),
  ('Logical_Or -> Logical_And Or_Quad Multiple_Ands','Logical_Or',3,'p_Logical_Or','Parser.py',105),
  ('Multiple_Ands -> OR Push_Or Logical_And Or_Quad Multiple_Ands','Multiple_Ands',5,'p_Multiple_Ands','Parser.py',112),
  ('Multiple_Ands -> Epsilon','Multiple_Ands',1,'p_Multiple_Ands','Parser.py',113),
  ('Or_Quad -> <empty>','Or_Quad',0,'p_Or_Quad','Parser.py',120),
  ('Push_Or -> <empty>','Push_Or',0,'p_Push_Or','Parser.py',172),
  ('Logical_And -> Logical_Not And_Quad Multiple_Nots','Logical_And',3,'p_Logical_And','Parser.py',182),
  ('Multiple_Nots -> AND Push_And Logical_Not And_Quad Multiple_Nots','Multiple_Nots',5,'p_Multiple_Nots','Parser.py',189),
  ('Multiple_Nots -> Epsilon','Multiple_Nots',1,'p_Multiple_Nots','Parser.py',190),
  ('And_Quad -> <empty>','And_Quad',0,'p_And_Quad','Parser.py',197),
  ('Push_And -> <empty>','Push_And',0,'p_Push_And','Parser.py',250),
  ('Logical_Not -> Relational','Logical_Not',1,'p_Logical_Not','Parser.py',260),
  ('Logical_Not -> NOT Push_Not Relational Not_Quad','Logical_Not',4,'p_Logical_Not','Parser.py',261),
  ('Not_Quad -> <empty>','Not_Quad',0,'p_Not_Quad','Parser.py',268),
  ('Push_Not -> <empty>','Push_Not',0,'p_Push_Not','Parser.py',320),
  ('Relational -> Expression','Relational',1,'p_Relational','Parser.py',330),
  ('Relational -> Expression LESS Push_Less Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',331),
  ('Relational -> Expression LESS_EQUAL Push_Less_Equal Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',332),
  ('Relational -> Expression GREATER Push_Greater Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',333),
  ('Relational -> Expression GREATER_EQUAL Push_Greater_Equal Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',334),
  ('Relational_Quad -> <empty>','Relational_Quad',0,'p_Relational_Quad','Parser.py',341),
  ('Push_Less -> <empty>','Push_Less',0,'p_Push_Less','Parser.py',394),
  ('Push_Less_Equal -> <empty>','Push_Less_Equal',0,'p_Push_Less_Equal','Parser.py',400),
  ('Push_Greater -> <empty>','Push_Greater',0,'p_Push_Greater','Parser.py',406),
  ('Push_Greater_Equal -> <empty>','Push_Greater_Equal',0,'p_Push_Greater_Equal','Parser.py',412),
  ('Expression -> Term Sum_Sub_Quad Multiple_Terms','Expression',3,'p_Expression','Parser.py',422),
  ('Multiple_Terms -> PLUS_SIGN Push_Plus_Sign Term Sum_Sub_Quad Multiple_Terms','Multiple_Terms',5,'p_Multiple_Terms','Parser.py',429),
  ('Multiple_Terms -> MINUS_SIGN Push_Minus_Sign Term Sum_Sub_Quad Multiple_Terms','Multiple_Terms',5,'p_Multiple_Terms','Parser.py',430),
  ('Multiple_Terms -> Epsilon','Multiple_Terms',1,'p_Multiple_Terms','Parser.py',431),
  ('Sum_Sub_Quad -> <empty>','Sum_Sub_Quad',0,'p_Sum_Sub_Quad','Parser.py',438),
  ('Push_Plus_Sign -> <empty>','Push_Plus_Sign',0,'p_Push_Plus_Sign','Parser.py',491),
  ('Push_Minus_Sign -> <empty>','Push_Minus_Sign',0,'p_Push_Minus_Sign','Parser.py',497),
  ('Term -> Factor Mult_Div_Mod_Quad Multiple_Factors','Term',3,'p_Term','Parser.py',507),
  ('Multiple_Factors -> TIMES_SIGN Push_Times_Sign Factor Mult_Div_Mod_Quad Multiple_Factors','Multiple_Factors',5,'p_Multiple_Factors','Parser.py',513),
  ('Multiple_Factors -> DIVIDE_SIGN Push_Divide_Sign Factor Mult_Div_Mod_Quad Multiple_Factors','Multiple_Factors',5,'p_Multiple_Factors','Parser.py',514),
  ('Multiple_Factors -> MOD_SIGN Push_Mod_Sign Factor Mult_Div_Mod_Quad Multiple_Factors','Multiple_Factors',5,'p_Multiple_Factors','Parser.py',515),
  ('Multiple_Factors -> Epsilon','Multiple_Factors',1,'p_Multiple_Factors','Parser.py',516),
  ('Mult_Div_Mod_Quad -> <empty>','Mult_Div_Mod_Quad',0,'p_Mult_Div_Mod_Quad','Parser.py',523),
  ('Push_Times_Sign -> <empty>','Push_Times_Sign',0,'p_Push_Times_Sign','Parser.py',577),
  ('Push_Divide_Sign -> <empty>','Push_Divide_Sign',0,'p_Push_Divide_Sign','Parser.py',583),
  ('Push_Mod_Sign -> <empty>','Push_Mod_Sign',0,'p_Push_Mod_Sign','Parser.py',589),
  ('Factor -> PAR_OPEN Push_False_Bottom Logical_Or PAR_CLOSE Pop_False_Bottom','Factor',5,'p_Factor','Parser.py',601),
  ('Factor -> Var_Cte','Factor',1,'p_Factor','Parser.py',602),
  ('Push_False_Bottom -> <empty>','Push_False_Bottom',0,'p_Push_False_Bottom','Parser.py',609),
  ('Pop_False_Bottom -> <empty>','Pop_False_Bottom',0,'p_Pop_False_Bottom','Parser.py',615),
  ('Var_Cte -> INT_CONST Save_Int_Const','Var_Cte',2,'p_Var_Cte','Parser.py',626),
  ('Var_Cte -> MINUS_SIGN INT_CONST Save_Neg_Int_Const','Var_Cte',3,'p_Var_Cte','Parser.py',627),
  ('Var_Cte -> FLOAT_CONST Save_Float_Const','Var_Cte',2,'p_Var_Cte','Parser.py',628),
  ('Var_Cte -> MINUS_SIGN FLOAT_CONST Save_Neg_Float_Const','Var_Cte',3,'p_Var_Cte','Parser.py',629),
  ('Var_Cte -> BOOL_CONST Save_Bool_Const','Var_Cte',2,'p_Var_Cte','Parser.py',630),
  ('Var_Cte -> STRING_CONST Save_String_Const','Var_Cte',2,'p_Var_Cte','Parser.py',631),
  ('Save_Int_Const -> <empty>','Save_Int_Const',0,'p_Save_Int_Const','Parser.py',638),
  ('Save_Neg_Int_Const -> <empty>','Save_Neg_Int_Const',0,'p_Save_Neg_Int_Const','Parser.py',657),
  ('Save_Float_Const -> <empty>','Save_Float_Const',0,'p_Save_Float_Const','Parser.py',676),
  ('Save_Neg_Float_Const -> <empty>','Save_Neg_Float_Const',0,'p_Save_Neg_Float_Const','Parser.py',695),
  ('Save_Bool_Const -> <empty>','Save_Bool_Const',0,'p_Save_Bool_Const','Parser.py',714),
  ('Save_String_Const -> <empty>','Save_String_Const',0,'p_Save_String_Const','Parser.py',733),
  ('Epsilon -> <empty>','Epsilon',0,'p_Epsilon','Parser.py',755),
]
