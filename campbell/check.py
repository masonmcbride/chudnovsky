from decimal import Decimal, getcontext

# Set precision (e.g., 300 digits)
getcontext().prec = 400

# Define your number as a Decimal

# one iteration
high_precision_number = Decimal('0.31830988618379067153776752674502872406891929148091289749533468811779359526845307018022760553250617191214568545351591607378582369222915730575593482146340075216566604192067140996354169274235589374076178264332378892871422107405200258046634446253211934544335193642371463100581757038529095970684331404835229864695397473275539830111836177442203222413805680484215465386786246258523024666796163402009653656896463835745451374540892703878158580982048146792895131982404363337656687738073918272220529871924289532775579522424784724174550100669366134661530888909553204892747828772598385756492958024440397888695262455662532006094874478203681250804268946545045082532439634510632945225168767594386106773196502170809441167225338240795133784735778629514948191203159571934187855980316493682934432858004354124272093618124860035312900545582648270480521491398508397625452379336245572206965102323252235359622058301981808073522461087998276605997649712408567483587912836407911202604239535221276353921110272963')

# two iterations
high_precision_number = Decimal('0.31830988618379067153776752674502872406891929148091289749533468811779359526845307018022760553250617191214568545351591607378582369222915730575593482146339967845847993387481815514615549279385061537743478579243479532338672478048344725802366476022844539951143188092378017380534791224097882187387568817105744619977773145900466709633538616367247494359352575988351848552346328057832985710633725335022285216349356372678395958486265155152342320105451088788532309843245761976762213274335565124601311080163517277522737751605221421484298818224076059593738623203129495142789985490173052400877593484532037112808917615448057553228075427657584185106830077586458376751813692591148714373639501702069188225618576327174496401495809311325646801997312604895154944302908914703220204901727158990120587049425024987213389556215447340830110373239868560885519872029890753925431200221006409823451632106234682728750923283679764349848199517732541444423217365591273254280228202079331417783927282630004097912175235119')

# https://www.piday.org/million/
PI = "3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912983367336244065664308602139494639522473719070217986094370277053921717629317675238467481846766940513200056812714526356082778577134275778960917363717872146844090122495343014654958537105079227968925892354201995611212902196086403441815981362977477130996051870721134999999837297804995105973173281609631859502445945534690830264252230825334468503526193118817101000313783875288658753320838142061717766914730359825349042875546873115956286388235378759375195778185778053217122680661300192787661119590921642019893809525720106548586327886593615338182796823030195203530185296899577362259941389124972177528347913151557485724245415069595082953311686172785588907509838175463746493931925506040092770167113900984882401285836160356370766010471018194295559619894676783744944825537977472684710404753464620804668425906949129331367702898915210475216205696602405803815019351125338243003558764024749647326391419927260426992279678235478163600934172164121992458631503028618297455570674983850549458858692699569092721079750930295532116534498720275596023648066549911988183479775356636980742654252786255181841757467289097777279380008164706001614524919217321721477235014144197356854816136115735255213347574184946843852332390739414333454776241686"

# Compute the reciprocal
reciprocal = 1 / high_precision_number

# Print the result
print(reciprocal)

reciprocal_digits = str(reciprocal)

# Build the comparison string and find the first difference
comparison = ""
difference_index = None
for i, (pi_digit, reciprocal_digit) in enumerate(zip(PI, reciprocal_digits)):
    if pi_digit == reciprocal_digit:
        comparison += "-"
    else:
        comparison += f"[COMPUTED]{reciprocal_digit}/[ACTUAL]{pi_digit}"
        if difference_index is None:
            difference_index = i

# Output the results
print("Comparison string:", comparison)
if difference_index is not None:
    print(f"First difference at index {difference_index}: PI='{PI[difference_index]}' Reciprocal='{reciprocal_digits[difference_index]}'")
else:
    print("No differences found within the compared range.")


