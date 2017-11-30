
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'TRIANGLE DRAW YELLOW WHILE GREEN EIF PRINT CYAN LINE RED STRING BLUE POINT PURPLE ORANGE PINK PLAY SQUARE POLYGON GRAY ELSE FUNC INPUT WHITE CIRCLE RECTANGLE IF AND INT FLOAT BOOL NOT BLACK MAGENTA OR INT_CONST FLOAT_CONST STRING_CONST BOOL_CONST COMMENT BLOCK_COMMENT ASSIGN PLUS_SIGN MINUS_SIGN TIMES_SIGN DIVIDE_SIGN MOD_SIGN LESS LESS_EQUAL GREATER GREATER_EQUAL EQUAL DIFF PAR_OPEN PAR_CLOSE CURLYB_OPEN CURLYB_CLOSE SQRB_OPEN SQRB_CLOSE COMMA SEMICOLON ID\n    Obi : Prev_To_Play Play\n    \n    Prev_To_Play : GoTo_Global_Vars Declare_Var GoTo_Play Prev_To_Play\n    | Epsilon\n    \n    GoTo_Global_Vars :\n    \n    GoTo_Play :\n    \n    Play : PLAY Play_Init PAR_OPEN PAR_CLOSE Statements_Block\n    \n    Play_Init :\n    \n    Statements_Block : CURLYB_OPEN Multiple_Statements CURLYB_CLOSE\n    \n    Multiple_Statements : Statement Multiple_Statements\n    | Epsilon\n    \n    Statement : Print\n    | Declare_Var\n    | Assignment\n    | While_Loop\n    | If_Eif_Else\n    | Draw_Stmt\n    \n    Draw_Stmt : DRAW Drawable SEMICOLON\n    \n    Drawable : Circle_Func\n    | Square_Func\n    \n    Circle_Func : CIRCLE PAR_OPEN Exp COMMA Exp COMMA Exp COMMA Selected_Color PAR_CLOSE\n    \n    Square_Func : SQUARE PAR_OPEN Exp COMMA Exp COMMA Exp COMMA Selected_Color PAR_CLOSE\n    \n    Selected_Color : RED\n    | GREEN\n    | BLUE\n    | YELLOW\n    | PURPLE\n    | WHITE\n    | BLACK\n    | ORANGE\n    | CYAN\n    | MAGENTA\n    | PINK\n    | GRAY\n    \n    Print : PRINT PAR_OPEN Exp PAR_CLOSE SEMICOLON\n    \n    If_Eif_Else : IF PAR_OPEN Exp PAR_CLOSE If_GoToF_Quad Statements_Block GoTo_Fill Eif_Recursion Optional_Else\n    \n    Eif_Recursion : EIF PAR_OPEN Exp PAR_CLOSE If_GoToF_Quad Statements_Block GoTo_Fill Eif_Recursion\n    | Epsilon\n    \n    Optional_Else : ELSE Statements_Block\n    | Epsilon\n    \n    If_GoToF_Quad :\n    \n    GoTo_Fill :\n    \n    While_Loop : WHILE Push_While_Jump PAR_OPEN Exp PAR_CLOSE While_Quad Statements_Block Fill_While_Quads\n    \n    Push_While_Jump :\n    \n    While_Quad :\n    \n    Fill_While_Quads :\n    \n    Declare_Var : Type ID SEMICOLON\n    | Type ID ASSIGN Push_Assign Exp SEMICOLON\n    \n    Type : INT\n    | FLOAT\n    | BOOL\n    | STRING\n    \n    Assignment : ID ASSIGN Push_Assign Exp SEMICOLON\n    \n    Push_Assign :\n    \n    Exp : Logical_Or\n    | Logical_Or EQUAL Push_Equal Logical_Or Equity_Quad\n    | Logical_Or DIFF Push_Diff Logical_Or Equity_Quad\n    \n    Equity_Quad :\n    \n    Push_Equal :\n    \n    Push_Diff :\n    \n    Logical_Or : Logical_And Or_Quad Multiple_Ands\n    \n    Multiple_Ands : OR Push_Or Logical_And Or_Quad Multiple_Ands\n    | Epsilon\n    \n    Or_Quad :\n    \n    Push_Or :\n    \n    Logical_And : Logical_Not And_Quad Multiple_Nots\n    \n    Multiple_Nots : AND Push_And Logical_Not And_Quad Multiple_Nots\n    | Epsilon\n    \n    And_Quad :\n    \n    Push_And :\n    \n    Logical_Not : Relational\n    | NOT Push_Not Relational Not_Quad\n    \n    Not_Quad :\n    \n    Push_Not :\n    \n    Relational : Expression\n    | Expression LESS Push_Less Expression Relational_Quad\n    | Expression LESS_EQUAL Push_Less_Equal Expression Relational_Quad\n    | Expression GREATER Push_Greater Expression Relational_Quad\n    | Expression GREATER_EQUAL Push_Greater_Equal Expression Relational_Quad\n    \n    Relational_Quad :\n    \n    Push_Less :\n    \n    Push_Less_Equal :\n    \n    Push_Greater :\n    \n    Push_Greater_Equal :\n    \n    Expression : Term Sum_Sub_Quad Multiple_Terms\n    \n    Multiple_Terms : PLUS_SIGN Push_Plus_Sign Term Sum_Sub_Quad Multiple_Terms\n    | MINUS_SIGN Push_Minus_Sign Term Sum_Sub_Quad Multiple_Terms\n    | Epsilon\n    \n    Sum_Sub_Quad :\n    \n    Push_Plus_Sign :\n    \n    Push_Minus_Sign :\n    \n    Term : Factor Mult_Div_Mod_Quad Multiple_Factors\n    \n    Multiple_Factors : TIMES_SIGN Push_Times_Sign Factor Mult_Div_Mod_Quad Multiple_Factors\n    | DIVIDE_SIGN Push_Divide_Sign Factor Mult_Div_Mod_Quad Multiple_Factors\n    | MOD_SIGN Push_Mod_Sign Factor Mult_Div_Mod_Quad Multiple_Factors\n    | Epsilon\n    \n    Mult_Div_Mod_Quad :\n    \n    Push_Times_Sign :\n    \n    Push_Divide_Sign :\n    \n    Push_Mod_Sign :\n    \n    Factor : PAR_OPEN Push_False_Bottom Exp PAR_CLOSE Pop_False_Bottom\n    | Var_Cte\n    \n    Push_False_Bottom :\n    \n    Pop_False_Bottom :\n    \n    Var_Cte : INT_CONST Save_Int_Const\n    | MINUS_SIGN INT_CONST Save_Neg_Int_Const\n    | FLOAT_CONST Save_Float_Const\n    | MINUS_SIGN FLOAT_CONST Save_Neg_Float_Const\n    | BOOL_CONST Save_Bool_Const\n    | STRING_CONST Save_String_Const\n    | ID Get_Id_Value\n    \n    Save_Int_Const :\n    \n    Save_Neg_Int_Const :\n    \n    Save_Float_Const :\n    \n    Save_Neg_Float_Const :\n    \n    Save_Bool_Const :\n    \n    Save_String_Const :\n    \n    Get_Id_Value :\n    \n    Epsilon :\n    '
    
_lr_action_items = {'TIMES_SIGN':([25,27,29,30,32,33,38,56,57,59,60,62,71,72,73,108,109,118,139,143,144,145,162,163,164,],[-113,-111,-115,-116,-96,-101,-117,-106,-104,-108,-109,94,-110,-112,-114,-105,-107,-103,-100,-96,-96,-96,94,94,94,]),'PAR_CLOSE':([16,25,26,27,28,29,30,31,32,33,34,35,37,38,56,57,58,59,60,61,62,65,71,72,73,86,88,89,90,91,96,97,101,102,108,109,110,115,117,118,125,126,128,129,130,131,132,135,139,140,141,142,143,144,145,146,147,148,149,150,151,152,159,160,161,162,163,164,165,170,171,172,173,174,175,176,193,194,195,196,197,198,199,200,201,202,203,204,205,206,208,],[20,-113,-70,-111,-68,-115,-116,-88,-96,-101,-54,-63,-74,-117,-106,-104,-118,-108,-109,-118,-118,-118,-110,-112,-114,118,-67,-65,-84,-87,-95,-91,-60,-62,-105,-107,-72,136,138,-103,-57,-57,-79,-79,-79,-79,-71,155,-100,-68,-88,-88,-96,-96,-96,-55,-56,-63,-75,-76,-78,-77,-118,-118,-118,-118,-118,-118,-118,-66,-86,-85,-92,-94,-93,-61,-24,-33,-26,-23,-25,-28,-32,209,-29,-27,-30,-31,-22,210,211,]),'LESS':([25,27,29,30,31,32,33,37,38,56,57,59,60,61,62,71,72,73,90,91,96,97,108,109,118,139,141,142,143,144,145,160,161,162,163,164,171,172,173,174,175,],[-113,-111,-115,-116,-88,-96,-101,67,-117,-106,-104,-108,-109,-118,-118,-110,-112,-114,-84,-87,-95,-91,-105,-107,-103,-100,-88,-88,-96,-96,-96,-118,-118,-118,-118,-118,-86,-85,-92,-94,-93,]),'DRAW':([18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-46,41,-11,41,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'YELLOW':([187,188,],[197,197,]),'WHILE':([18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-46,43,-11,43,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'PAR_OPEN':([6,13,19,21,24,40,43,45,53,55,63,64,67,68,69,70,74,76,78,80,82,84,85,87,92,93,94,95,98,99,100,103,104,105,106,107,111,112,114,116,119,120,121,122,123,124,127,153,154,177,178,186,192,],[-7,16,-53,24,-102,-73,-43,82,85,24,-58,-59,-80,-81,-83,-82,24,111,112,114,24,-53,24,-69,-90,-89,-97,-99,-98,24,24,-64,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,192,24,]),'FLOAT_CONST':([19,21,24,39,40,55,63,64,67,68,69,70,74,82,84,85,87,92,93,94,95,98,99,100,103,104,105,106,107,111,112,114,116,119,120,121,122,123,124,127,153,154,177,178,192,],[-53,25,-102,73,-73,25,-58,-59,-80,-81,-83,-82,25,25,-53,25,-69,-90,-89,-97,-99,-98,25,25,-64,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'EIF':([83,169,180,213,214,],[-8,-41,186,-41,186,]),'PRINT':([18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-46,45,-11,45,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'DIFF':([25,26,27,28,29,30,31,32,33,34,35,37,38,56,57,58,59,60,61,62,65,71,72,73,88,89,90,91,96,97,101,102,108,109,110,118,128,129,130,131,132,139,140,141,142,143,144,145,148,149,150,151,152,159,160,161,162,163,164,165,170,171,172,173,174,175,176,],[-113,-70,-111,-68,-115,-116,-88,-96,-101,64,-63,-74,-117,-106,-104,-118,-108,-109,-118,-118,-118,-110,-112,-114,-67,-65,-84,-87,-95,-91,-60,-62,-105,-107,-72,-103,-79,-79,-79,-79,-71,-100,-68,-88,-88,-96,-96,-96,-63,-75,-76,-78,-77,-118,-118,-118,-118,-118,-118,-118,-66,-86,-85,-92,-94,-93,-61,]),'PLUS_SIGN':([25,27,29,30,31,32,33,38,56,57,59,60,61,62,71,72,73,96,97,108,109,118,139,141,142,143,144,145,160,161,162,163,164,173,174,175,],[-113,-111,-115,-116,-88,-96,-101,-117,-106,-104,-108,-109,93,-118,-110,-112,-114,-95,-91,-105,-107,-103,-100,-88,-88,-96,-96,-96,93,93,-118,-118,-118,-92,-94,-93,]),'RED':([187,188,],[205,205,]),'STRING_CONST':([19,21,24,40,55,63,64,67,68,69,70,74,82,84,85,87,92,93,94,95,98,99,100,103,104,105,106,107,111,112,114,116,119,120,121,122,123,124,127,153,154,177,178,192,],[-53,30,-102,-73,30,-58,-59,-80,-81,-83,-82,30,30,-53,30,-69,-90,-89,-97,-99,-98,30,30,-64,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'GRAY':([187,188,],[194,194,]),'INT_CONST':([19,21,24,39,40,55,63,64,67,68,69,70,74,82,84,85,87,92,93,94,95,98,99,100,103,104,105,106,107,111,112,114,116,119,120,121,122,123,124,127,153,154,177,178,192,],[-53,27,-102,72,-73,27,-58,-59,-80,-81,-83,-82,27,27,-53,27,-69,-90,-89,-97,-99,-98,27,27,-64,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'SEMICOLON':([15,25,26,27,28,29,30,31,32,33,34,35,36,37,38,56,57,58,59,60,61,62,65,71,72,73,75,77,79,88,89,90,91,96,97,101,102,108,109,110,118,125,126,128,129,130,131,132,136,137,139,140,141,142,143,144,145,146,147,148,149,150,151,152,159,160,161,162,163,164,165,170,171,172,173,174,175,176,209,210,],[18,-113,-70,-111,-68,-115,-116,-88,-96,-101,-54,-63,66,-74,-117,-106,-104,-118,-108,-109,-118,-118,-118,-110,-112,-114,-18,-19,113,-67,-65,-84,-87,-95,-91,-60,-62,-105,-107,-72,-103,-57,-57,-79,-79,-79,-79,-71,156,157,-100,-68,-88,-88,-96,-96,-96,-55,-56,-63,-75,-76,-78,-77,-118,-118,-118,-118,-118,-118,-118,-66,-86,-85,-92,-94,-93,-61,-21,-20,]),'MOD_SIGN':([25,27,29,30,32,33,38,56,57,59,60,62,71,72,73,108,109,118,139,143,144,145,162,163,164,],[-113,-111,-115,-116,-96,-101,-117,-106,-104,-108,-109,95,-110,-112,-114,-105,-107,-103,-100,-96,-96,-96,95,95,95,]),'BOOL_CONST':([19,21,24,40,55,63,64,67,68,69,70,74,82,84,85,87,92,93,94,95,98,99,100,103,104,105,106,107,111,112,114,116,119,120,121,122,123,124,127,153,154,177,178,192,],[-53,29,-102,-73,29,-58,-59,-80,-81,-83,-82,29,29,-53,29,-69,-90,-89,-97,-99,-98,29,29,-64,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'MAGENTA':([187,188,],[204,204,]),'COMMA':([25,26,27,28,29,30,31,32,33,34,35,37,38,56,57,58,59,60,61,62,65,71,72,73,88,89,90,91,96,97,101,102,108,109,110,118,125,126,128,129,130,131,132,133,134,139,140,141,142,143,144,145,146,147,148,149,150,151,152,159,160,161,162,163,164,165,166,167,170,171,172,173,174,175,176,181,182,],[-113,-70,-111,-68,-115,-116,-88,-96,-101,-54,-63,-74,-117,-106,-104,-118,-108,-109,-118,-118,-118,-110,-112,-114,-67,-65,-84,-87,-95,-91,-60,-62,-105,-107,-72,-103,-57,-57,-79,-79,-79,-79,-71,153,154,-100,-68,-88,-88,-96,-96,-96,-55,-56,-63,-75,-76,-78,-77,-118,-118,-118,-118,-118,-118,-118,177,178,-66,-86,-85,-92,-94,-93,-61,187,188,]),'ORANGE':([187,188,],[201,201,]),'BLACK':([187,188,],[198,198,]),'CYAN':([187,188,],[203,203,]),'ASSIGN':([15,52,],[19,84,]),'$end':([1,5,22,83,],[0,-1,-6,-8,]),'BLUE':([187,188,],[193,193,]),'PLAY':([0,2,3,9,14,17,18,66,],[-118,-3,6,-5,-118,-2,-46,-47,]),'SQUARE':([41,],[76,]),'STRING':([0,4,9,14,18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-4,7,-5,-4,-46,7,-11,7,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'EQUAL':([25,26,27,28,29,30,31,32,33,34,35,37,38,56,57,58,59,60,61,62,65,71,72,73,88,89,90,91,96,97,101,102,108,109,110,118,128,129,130,131,132,139,140,141,142,143,144,145,148,149,150,151,152,159,160,161,162,163,164,165,170,171,172,173,174,175,176,],[-113,-70,-111,-68,-115,-116,-88,-96,-101,63,-63,-74,-117,-106,-104,-118,-108,-109,-118,-118,-118,-110,-112,-114,-67,-65,-84,-87,-95,-91,-60,-62,-105,-107,-72,-103,-79,-79,-79,-79,-71,-100,-68,-88,-88,-96,-96,-96,-63,-75,-76,-78,-77,-118,-118,-118,-118,-118,-118,-118,-66,-86,-85,-92,-94,-93,-61,]),'LESS_EQUAL':([25,27,29,30,31,32,33,37,38,56,57,59,60,61,62,71,72,73,90,91,96,97,108,109,118,139,141,142,143,144,145,160,161,162,163,164,171,172,173,174,175,],[-113,-111,-115,-116,-88,-96,-101,68,-117,-106,-104,-108,-109,-118,-118,-110,-112,-114,-84,-87,-95,-91,-105,-107,-103,-100,-88,-88,-96,-96,-96,-118,-118,-118,-118,-118,-86,-85,-92,-94,-93,]),'WHITE':([187,188,],[202,202,]),'ELSE':([83,169,180,184,185,213,214,215,],[-8,-41,-118,190,-37,-41,-118,-36,]),'ID':([7,8,10,11,12,18,19,21,23,24,40,42,44,46,49,50,51,54,55,63,64,66,67,68,69,70,74,82,83,84,85,87,92,93,94,95,98,99,100,103,104,105,106,107,111,112,113,114,116,119,120,121,122,123,124,127,153,154,156,157,169,177,178,179,180,183,184,185,189,191,192,207,213,214,215,],[-51,-48,-49,-50,15,-46,-53,38,52,-102,-73,-11,52,-16,-14,-12,-15,-13,38,-58,-59,-47,-80,-81,-83,-82,38,38,-8,-53,38,-69,-90,-89,-97,-99,-98,38,38,-64,38,38,38,38,38,38,-17,38,38,38,38,38,38,38,38,38,38,38,-34,-52,-41,38,38,-45,-118,-42,-118,-37,-35,-39,38,-38,-41,-118,-36,]),'IF':([18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-46,53,-11,53,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'AND':([25,26,27,28,29,30,31,32,33,37,38,56,57,58,59,60,61,62,71,72,73,90,91,96,97,108,109,110,118,128,129,130,131,132,139,140,141,142,143,144,145,149,150,151,152,159,160,161,162,163,164,171,172,173,174,175,],[-113,-70,-111,-68,-115,-116,-88,-96,-101,-74,-117,-106,-104,87,-108,-109,-118,-118,-110,-112,-114,-84,-87,-95,-91,-105,-107,-72,-103,-79,-79,-79,-79,-71,-100,-68,-88,-88,-96,-96,-96,-75,-76,-78,-77,87,-118,-118,-118,-118,-118,-86,-85,-92,-94,-93,]),'GREATER_EQUAL':([25,27,29,30,31,32,33,37,38,56,57,59,60,61,62,71,72,73,90,91,96,97,108,109,118,139,141,142,143,144,145,160,161,162,163,164,171,172,173,174,175,],[-113,-111,-115,-116,-88,-96,-101,69,-117,-106,-104,-108,-109,-118,-118,-110,-112,-114,-84,-87,-95,-91,-105,-107,-103,-100,-88,-88,-96,-96,-96,-118,-118,-118,-118,-118,-86,-85,-92,-94,-93,]),'GREATER':([25,27,29,30,31,32,33,37,38,56,57,59,60,61,62,71,72,73,90,91,96,97,108,109,118,139,141,142,143,144,145,160,161,162,163,164,171,172,173,174,175,],[-113,-111,-115,-116,-88,-96,-101,70,-117,-106,-104,-108,-109,-118,-118,-110,-112,-114,-84,-87,-95,-91,-105,-107,-103,-100,-88,-88,-96,-96,-96,-118,-118,-118,-118,-118,-86,-85,-92,-94,-93,]),'INT':([0,4,9,14,18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-4,8,-5,-4,-46,8,-11,8,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'FLOAT':([0,4,9,14,18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-4,10,-5,-4,-46,10,-11,10,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'OR':([25,26,27,28,29,30,31,32,33,35,37,38,56,57,58,59,60,61,62,65,71,72,73,88,89,90,91,96,97,108,109,110,118,128,129,130,131,132,139,140,141,142,143,144,145,148,149,150,151,152,159,160,161,162,163,164,165,170,171,172,173,174,175,],[-113,-70,-111,-68,-115,-116,-88,-96,-101,-63,-74,-117,-106,-104,-118,-108,-109,-118,-118,103,-110,-112,-114,-67,-65,-84,-87,-95,-91,-105,-107,-72,-103,-79,-79,-79,-79,-71,-100,-68,-88,-88,-96,-96,-96,-63,-75,-76,-78,-77,-118,-118,-118,-118,-118,-118,103,-66,-86,-85,-92,-94,-93,]),'PURPLE':([187,188,],[195,195,]),'BOOL':([0,4,9,14,18,23,42,44,46,49,50,51,54,66,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-4,11,-5,-4,-46,11,-11,11,-16,-14,-12,-15,-13,-47,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),'DIVIDE_SIGN':([25,27,29,30,32,33,38,56,57,59,60,62,71,72,73,108,109,118,139,143,144,145,162,163,164,],[-113,-111,-115,-116,-96,-101,-117,-106,-104,-108,-109,98,-110,-112,-114,-105,-107,-103,-100,-96,-96,-96,98,98,98,]),'MINUS_SIGN':([19,21,24,25,27,29,30,31,32,33,38,40,55,56,57,59,60,61,62,63,64,67,68,69,70,71,72,73,74,82,84,85,87,92,93,94,95,96,97,98,99,100,103,104,105,106,107,108,109,111,112,114,116,118,119,120,121,122,123,124,127,139,141,142,143,144,145,153,154,160,161,162,163,164,173,174,175,177,178,192,],[-53,39,-102,-113,-111,-115,-116,-88,-96,-101,-117,-73,39,-106,-104,-108,-109,92,-118,-58,-59,-80,-81,-83,-82,-110,-112,-114,39,39,-53,39,-69,-90,-89,-97,-99,-95,-91,-98,39,39,-64,39,39,39,39,-105,-107,39,39,39,39,-103,39,39,39,39,39,39,39,-100,-88,-88,-96,-96,-96,39,39,92,92,-118,-118,-118,-92,-94,-93,39,39,39,]),'PINK':([187,188,],[199,199,]),'NOT':([19,21,24,55,63,64,82,84,85,87,99,100,103,111,112,114,116,119,127,153,154,177,178,192,],[-53,40,-102,40,-58,-59,40,-53,40,-69,40,40,-64,40,40,40,40,40,40,40,40,40,40,40,]),'GREEN':([187,188,],[196,196,]),'CIRCLE':([41,],[78,]),'CURLYB_OPEN':([20,138,155,158,168,190,211,212,],[23,-40,-44,23,23,23,-40,23,]),'CURLYB_CLOSE':([18,23,42,44,46,47,48,49,50,51,54,66,81,83,113,156,157,169,179,180,183,184,185,189,191,207,213,214,215,],[-46,-118,-11,-118,-16,-10,83,-14,-12,-15,-13,-47,-9,-8,-17,-34,-52,-41,-45,-118,-42,-118,-37,-35,-39,-38,-41,-118,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Push_Minus_Sign':([92,],[120,]),'Push_Greater':([70,],[107,]),'Multiple_Ands':([65,165,],[101,176,]),'Push_While_Jump':([43,],[80,]),'Push_Less_Equal':([68,],[105,]),'Not_Quad':([110,],[132,]),'Push_Greater_Equal':([69,],[106,]),'Term':([21,55,74,82,85,99,100,104,105,106,107,111,112,114,116,119,120,121,127,153,154,177,178,192,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,141,142,31,31,31,31,31,31,]),'Multiple_Nots':([58,159,],[89,170,]),'Equity_Quad':([125,126,],[146,147,]),'Statement':([23,44,],[44,44,]),'Factor':([21,55,74,82,85,99,100,104,105,106,107,111,112,114,116,119,120,121,122,123,124,127,153,154,177,178,192,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,143,144,145,32,32,32,32,32,32,]),'Print':([23,44,],[42,42,]),'Relational':([21,55,74,82,85,99,100,111,112,114,116,119,127,153,154,177,178,192,],[26,26,110,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'Mult_Div_Mod_Quad':([32,143,144,145,],[62,162,163,164,]),'Type':([4,23,44,],[12,12,12,]),'Drawable':([41,],[79,]),'Sum_Sub_Quad':([31,141,142,],[61,160,161,]),'Or_Quad':([35,148,],[65,165,]),'Play':([3,],[5,]),'Logical_Not':([21,55,82,85,99,100,111,112,114,116,119,127,153,154,177,178,192,],[28,28,28,28,28,28,28,28,28,28,140,28,28,28,28,28,28,]),'Push_And':([87,],[119,]),'Save_String_Const':([30,],[60,]),'Epsilon':([0,14,23,44,58,61,62,65,159,160,161,162,163,164,165,180,184,214,],[2,2,47,47,88,91,96,102,88,91,91,96,96,96,102,185,191,185,]),'Push_Times_Sign':([94,],[122,]),'GoTo_Play':([9,],[14,]),'Fill_While_Quads':([179,],[183,]),'Push_Mod_Sign':([95,],[123,]),'Multiple_Factors':([62,162,163,164,],[97,173,174,175,]),'Get_Id_Value':([38,],[71,]),'Push_Or':([103,],[127,]),'Save_Bool_Const':([29,],[59,]),'Multiple_Statements':([23,44,],[48,81,]),'And_Quad':([28,140,],[58,159,]),'Push_Less':([67,],[104,]),'While_Loop':([23,44,],[49,49,]),'Obi':([0,],[1,]),'Save_Float_Const':([25,],[56,]),'Square_Func':([41,],[77,]),'Save_Int_Const':([27,],[57,]),'Draw_Stmt':([23,44,],[46,46,]),'Var_Cte':([21,55,74,82,85,99,100,104,105,106,107,111,112,114,116,119,120,121,122,123,124,127,153,154,177,178,192,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'Logical_Or':([21,55,82,85,99,100,111,112,114,116,153,154,177,178,192,],[34,34,34,34,125,126,34,34,34,34,34,34,34,34,34,]),'Play_Init':([6,],[13,]),'Declare_Var':([4,23,44,],[9,50,50,]),'Logical_And':([21,55,82,85,99,100,111,112,114,116,127,153,154,177,178,192,],[35,35,35,35,35,35,35,35,35,35,148,35,35,35,35,35,]),'Exp':([21,55,82,85,111,112,114,116,153,154,177,178,192,],[36,86,115,117,133,134,135,137,166,167,181,182,208,]),'If_Eif_Else':([23,44,],[51,51,]),'Push_Not':([40,],[74,]),'Expression':([21,55,74,82,85,99,100,104,105,106,107,111,112,114,116,119,127,153,154,177,178,192,],[37,37,37,37,37,37,37,128,129,130,131,37,37,37,37,37,37,37,37,37,37,37,]),'While_Quad':([155,],[168,]),'Save_Neg_Int_Const':([72,],[108,]),'Circle_Func':([41,],[75,]),'Push_Assign':([19,84,],[21,116,]),'Multiple_Terms':([61,160,161,],[90,171,172,]),'If_GoToF_Quad':([138,211,],[158,212,]),'Optional_Else':([184,],[189,]),'Save_Neg_Float_Const':([73,],[109,]),'Statements_Block':([20,158,168,190,212,],[22,169,179,207,213,]),'Push_Diff':([64,],[100,]),'Eif_Recursion':([180,214,],[184,215,]),'Push_Plus_Sign':([93,],[121,]),'Relational_Quad':([128,129,130,131,],[149,150,151,152,]),'Prev_To_Play':([0,14,],[3,17,]),'GoTo_Fill':([169,213,],[180,214,]),'Assignment':([23,44,],[54,54,]),'Push_Divide_Sign':([98,],[124,]),'Selected_Color':([187,188,],[200,206,]),'Pop_False_Bottom':([118,],[139,]),'Push_False_Bottom':([24,],[55,]),'Push_Equal':([63,],[99,]),'GoTo_Global_Vars':([0,14,],[4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Obi","S'",1,None,None,None),
  ('Obi -> Prev_To_Play Play','Obi',2,'p_Obi','Parser.py',54),
  ('Prev_To_Play -> GoTo_Global_Vars Declare_Var GoTo_Play Prev_To_Play','Prev_To_Play',4,'p_Prev_To_Play','Parser.py',60),
  ('Prev_To_Play -> Epsilon','Prev_To_Play',1,'p_Prev_To_Play','Parser.py',61),
  ('GoTo_Global_Vars -> <empty>','GoTo_Global_Vars',0,'p_GoTo_Global_Vars','Parser.py',68),
  ('GoTo_Play -> <empty>','GoTo_Play',0,'p_GoTo_Play','Parser.py',74),
  ('Play -> PLAY Play_Init PAR_OPEN PAR_CLOSE Statements_Block','Play',5,'p_Play','Parser.py',88),
  ('Play_Init -> <empty>','Play_Init',0,'p_Play_Init','Parser.py',93),
  ('Statements_Block -> CURLYB_OPEN Multiple_Statements CURLYB_CLOSE','Statements_Block',3,'p_Statements_Block','Parser.py',111),
  ('Multiple_Statements -> Statement Multiple_Statements','Multiple_Statements',2,'p_Multiple_Statements','Parser.py',117),
  ('Multiple_Statements -> Epsilon','Multiple_Statements',1,'p_Multiple_Statements','Parser.py',118),
  ('Statement -> Print','Statement',1,'p_Statement','Parser.py',124),
  ('Statement -> Declare_Var','Statement',1,'p_Statement','Parser.py',125),
  ('Statement -> Assignment','Statement',1,'p_Statement','Parser.py',126),
  ('Statement -> While_Loop','Statement',1,'p_Statement','Parser.py',127),
  ('Statement -> If_Eif_Else','Statement',1,'p_Statement','Parser.py',128),
  ('Statement -> Draw_Stmt','Statement',1,'p_Statement','Parser.py',129),
  ('Draw_Stmt -> DRAW Drawable SEMICOLON','Draw_Stmt',3,'p_Draw_Stmt','Parser.py',143),
  ('Drawable -> Circle_Func','Drawable',1,'p_Drawable','Parser.py',149),
  ('Drawable -> Square_Func','Drawable',1,'p_Drawable','Parser.py',150),
  ('Circle_Func -> CIRCLE PAR_OPEN Exp COMMA Exp COMMA Exp COMMA Selected_Color PAR_CLOSE','Circle_Func',10,'p_Circle_Func','Parser.py',164),
  ('Square_Func -> SQUARE PAR_OPEN Exp COMMA Exp COMMA Exp COMMA Selected_Color PAR_CLOSE','Square_Func',10,'p_Square_Func','Parser.py',205),
  ('Selected_Color -> RED','Selected_Color',1,'p_Selected_Color','Parser.py',243),
  ('Selected_Color -> GREEN','Selected_Color',1,'p_Selected_Color','Parser.py',244),
  ('Selected_Color -> BLUE','Selected_Color',1,'p_Selected_Color','Parser.py',245),
  ('Selected_Color -> YELLOW','Selected_Color',1,'p_Selected_Color','Parser.py',246),
  ('Selected_Color -> PURPLE','Selected_Color',1,'p_Selected_Color','Parser.py',247),
  ('Selected_Color -> WHITE','Selected_Color',1,'p_Selected_Color','Parser.py',248),
  ('Selected_Color -> BLACK','Selected_Color',1,'p_Selected_Color','Parser.py',249),
  ('Selected_Color -> ORANGE','Selected_Color',1,'p_Selected_Color','Parser.py',250),
  ('Selected_Color -> CYAN','Selected_Color',1,'p_Selected_Color','Parser.py',251),
  ('Selected_Color -> MAGENTA','Selected_Color',1,'p_Selected_Color','Parser.py',252),
  ('Selected_Color -> PINK','Selected_Color',1,'p_Selected_Color','Parser.py',253),
  ('Selected_Color -> GRAY','Selected_Color',1,'p_Selected_Color','Parser.py',254),
  ('Print -> PRINT PAR_OPEN Exp PAR_CLOSE SEMICOLON','Print',5,'p_Print','Parser.py',268),
  ('If_Eif_Else -> IF PAR_OPEN Exp PAR_CLOSE If_GoToF_Quad Statements_Block GoTo_Fill Eif_Recursion Optional_Else','If_Eif_Else',9,'p_If_Eif_Else','Parser.py',285),
  ('Eif_Recursion -> EIF PAR_OPEN Exp PAR_CLOSE If_GoToF_Quad Statements_Block GoTo_Fill Eif_Recursion','Eif_Recursion',8,'p_Eif_Recursion','Parser.py',296),
  ('Eif_Recursion -> Epsilon','Eif_Recursion',1,'p_Eif_Recursion','Parser.py',297),
  ('Optional_Else -> ELSE Statements_Block','Optional_Else',2,'p_Optional_Else','Parser.py',303),
  ('Optional_Else -> Epsilon','Optional_Else',1,'p_Optional_Else','Parser.py',304),
  ('If_GoToF_Quad -> <empty>','If_GoToF_Quad',0,'p_If_GoToF_Quad','Parser.py',311),
  ('GoTo_Fill -> <empty>','GoTo_Fill',0,'p_GoTo_Fill','Parser.py',331),
  ('While_Loop -> WHILE Push_While_Jump PAR_OPEN Exp PAR_CLOSE While_Quad Statements_Block Fill_While_Quads','While_Loop',8,'p_While_Loop','Parser.py',356),
  ('Push_While_Jump -> <empty>','Push_While_Jump',0,'p_Push_While_Jump','Parser.py',362),
  ('While_Quad -> <empty>','While_Quad',0,'p_While_Quad','Parser.py',368),
  ('Fill_While_Quads -> <empty>','Fill_While_Quads',0,'p_Fill_While_Quads','Parser.py',388),
  ('Declare_Var -> Type ID SEMICOLON','Declare_Var',3,'p_Declare_Var','Parser.py',409),
  ('Declare_Var -> Type ID ASSIGN Push_Assign Exp SEMICOLON','Declare_Var',6,'p_Declare_Var','Parser.py',410),
  ('Type -> INT','Type',1,'p_Type','Parser.py',449),
  ('Type -> FLOAT','Type',1,'p_Type','Parser.py',450),
  ('Type -> BOOL','Type',1,'p_Type','Parser.py',451),
  ('Type -> STRING','Type',1,'p_Type','Parser.py',452),
  ('Assignment -> ID ASSIGN Push_Assign Exp SEMICOLON','Assignment',5,'p_Assignment','Parser.py',463),
  ('Push_Assign -> <empty>','Push_Assign',0,'p_Push_assign','Parser.py',498),
  ('Exp -> Logical_Or','Exp',1,'p_Exp','Parser.py',510),
  ('Exp -> Logical_Or EQUAL Push_Equal Logical_Or Equity_Quad','Exp',5,'p_Exp','Parser.py',511),
  ('Exp -> Logical_Or DIFF Push_Diff Logical_Or Equity_Quad','Exp',5,'p_Exp','Parser.py',512),
  ('Equity_Quad -> <empty>','Equity_Quad',0,'p_Equity_Quad','Parser.py',519),
  ('Push_Equal -> <empty>','Push_Equal',0,'p_Push_Equal','Parser.py',572),
  ('Push_Diff -> <empty>','Push_Diff',0,'p_Push_Diff','Parser.py',578),
  ('Logical_Or -> Logical_And Or_Quad Multiple_Ands','Logical_Or',3,'p_Logical_Or','Parser.py',588),
  ('Multiple_Ands -> OR Push_Or Logical_And Or_Quad Multiple_Ands','Multiple_Ands',5,'p_Multiple_Ands','Parser.py',595),
  ('Multiple_Ands -> Epsilon','Multiple_Ands',1,'p_Multiple_Ands','Parser.py',596),
  ('Or_Quad -> <empty>','Or_Quad',0,'p_Or_Quad','Parser.py',603),
  ('Push_Or -> <empty>','Push_Or',0,'p_Push_Or','Parser.py',655),
  ('Logical_And -> Logical_Not And_Quad Multiple_Nots','Logical_And',3,'p_Logical_And','Parser.py',665),
  ('Multiple_Nots -> AND Push_And Logical_Not And_Quad Multiple_Nots','Multiple_Nots',5,'p_Multiple_Nots','Parser.py',672),
  ('Multiple_Nots -> Epsilon','Multiple_Nots',1,'p_Multiple_Nots','Parser.py',673),
  ('And_Quad -> <empty>','And_Quad',0,'p_And_Quad','Parser.py',680),
  ('Push_And -> <empty>','Push_And',0,'p_Push_And','Parser.py',733),
  ('Logical_Not -> Relational','Logical_Not',1,'p_Logical_Not','Parser.py',743),
  ('Logical_Not -> NOT Push_Not Relational Not_Quad','Logical_Not',4,'p_Logical_Not','Parser.py',744),
  ('Not_Quad -> <empty>','Not_Quad',0,'p_Not_Quad','Parser.py',751),
  ('Push_Not -> <empty>','Push_Not',0,'p_Push_Not','Parser.py',803),
  ('Relational -> Expression','Relational',1,'p_Relational','Parser.py',813),
  ('Relational -> Expression LESS Push_Less Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',814),
  ('Relational -> Expression LESS_EQUAL Push_Less_Equal Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',815),
  ('Relational -> Expression GREATER Push_Greater Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',816),
  ('Relational -> Expression GREATER_EQUAL Push_Greater_Equal Expression Relational_Quad','Relational',5,'p_Relational','Parser.py',817),
  ('Relational_Quad -> <empty>','Relational_Quad',0,'p_Relational_Quad','Parser.py',824),
  ('Push_Less -> <empty>','Push_Less',0,'p_Push_Less','Parser.py',877),
  ('Push_Less_Equal -> <empty>','Push_Less_Equal',0,'p_Push_Less_Equal','Parser.py',883),
  ('Push_Greater -> <empty>','Push_Greater',0,'p_Push_Greater','Parser.py',889),
  ('Push_Greater_Equal -> <empty>','Push_Greater_Equal',0,'p_Push_Greater_Equal','Parser.py',895),
  ('Expression -> Term Sum_Sub_Quad Multiple_Terms','Expression',3,'p_Expression','Parser.py',905),
  ('Multiple_Terms -> PLUS_SIGN Push_Plus_Sign Term Sum_Sub_Quad Multiple_Terms','Multiple_Terms',5,'p_Multiple_Terms','Parser.py',912),
  ('Multiple_Terms -> MINUS_SIGN Push_Minus_Sign Term Sum_Sub_Quad Multiple_Terms','Multiple_Terms',5,'p_Multiple_Terms','Parser.py',913),
  ('Multiple_Terms -> Epsilon','Multiple_Terms',1,'p_Multiple_Terms','Parser.py',914),
  ('Sum_Sub_Quad -> <empty>','Sum_Sub_Quad',0,'p_Sum_Sub_Quad','Parser.py',921),
  ('Push_Plus_Sign -> <empty>','Push_Plus_Sign',0,'p_Push_Plus_Sign','Parser.py',974),
  ('Push_Minus_Sign -> <empty>','Push_Minus_Sign',0,'p_Push_Minus_Sign','Parser.py',980),
  ('Term -> Factor Mult_Div_Mod_Quad Multiple_Factors','Term',3,'p_Term','Parser.py',990),
  ('Multiple_Factors -> TIMES_SIGN Push_Times_Sign Factor Mult_Div_Mod_Quad Multiple_Factors','Multiple_Factors',5,'p_Multiple_Factors','Parser.py',996),
  ('Multiple_Factors -> DIVIDE_SIGN Push_Divide_Sign Factor Mult_Div_Mod_Quad Multiple_Factors','Multiple_Factors',5,'p_Multiple_Factors','Parser.py',997),
  ('Multiple_Factors -> MOD_SIGN Push_Mod_Sign Factor Mult_Div_Mod_Quad Multiple_Factors','Multiple_Factors',5,'p_Multiple_Factors','Parser.py',998),
  ('Multiple_Factors -> Epsilon','Multiple_Factors',1,'p_Multiple_Factors','Parser.py',999),
  ('Mult_Div_Mod_Quad -> <empty>','Mult_Div_Mod_Quad',0,'p_Mult_Div_Mod_Quad','Parser.py',1006),
  ('Push_Times_Sign -> <empty>','Push_Times_Sign',0,'p_Push_Times_Sign','Parser.py',1060),
  ('Push_Divide_Sign -> <empty>','Push_Divide_Sign',0,'p_Push_Divide_Sign','Parser.py',1066),
  ('Push_Mod_Sign -> <empty>','Push_Mod_Sign',0,'p_Push_Mod_Sign','Parser.py',1072),
  ('Factor -> PAR_OPEN Push_False_Bottom Exp PAR_CLOSE Pop_False_Bottom','Factor',5,'p_Factor','Parser.py',1084),
  ('Factor -> Var_Cte','Factor',1,'p_Factor','Parser.py',1085),
  ('Push_False_Bottom -> <empty>','Push_False_Bottom',0,'p_Push_False_Bottom','Parser.py',1092),
  ('Pop_False_Bottom -> <empty>','Pop_False_Bottom',0,'p_Pop_False_Bottom','Parser.py',1098),
  ('Var_Cte -> INT_CONST Save_Int_Const','Var_Cte',2,'p_Var_Cte','Parser.py',1109),
  ('Var_Cte -> MINUS_SIGN INT_CONST Save_Neg_Int_Const','Var_Cte',3,'p_Var_Cte','Parser.py',1110),
  ('Var_Cte -> FLOAT_CONST Save_Float_Const','Var_Cte',2,'p_Var_Cte','Parser.py',1111),
  ('Var_Cte -> MINUS_SIGN FLOAT_CONST Save_Neg_Float_Const','Var_Cte',3,'p_Var_Cte','Parser.py',1112),
  ('Var_Cte -> BOOL_CONST Save_Bool_Const','Var_Cte',2,'p_Var_Cte','Parser.py',1113),
  ('Var_Cte -> STRING_CONST Save_String_Const','Var_Cte',2,'p_Var_Cte','Parser.py',1114),
  ('Var_Cte -> ID Get_Id_Value','Var_Cte',2,'p_Var_Cte','Parser.py',1115),
  ('Save_Int_Const -> <empty>','Save_Int_Const',0,'p_Save_Int_Const','Parser.py',1122),
  ('Save_Neg_Int_Const -> <empty>','Save_Neg_Int_Const',0,'p_Save_Neg_Int_Const','Parser.py',1141),
  ('Save_Float_Const -> <empty>','Save_Float_Const',0,'p_Save_Float_Const','Parser.py',1160),
  ('Save_Neg_Float_Const -> <empty>','Save_Neg_Float_Const',0,'p_Save_Neg_Float_Const','Parser.py',1179),
  ('Save_Bool_Const -> <empty>','Save_Bool_Const',0,'p_Save_Bool_Const','Parser.py',1198),
  ('Save_String_Const -> <empty>','Save_String_Const',0,'p_Save_String_Const','Parser.py',1217),
  ('Get_Id_Value -> <empty>','Get_Id_Value',0,'p_Get_Id_Value','Parser.py',1236),
  ('Epsilon -> <empty>','Epsilon',0,'p_Epsilon','Parser.py',1263),
]
