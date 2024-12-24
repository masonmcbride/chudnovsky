default(realprecision, 1000); 
lambda1105=((sqrt(5) + 1)/2)^12*(4 + sqrt(17))^3*((15 + sqrt(221))/2)^3*(8 + sqrt(65))^3;
boldJ3315=-((64*lambda1105^2)/((lambda1105^2- 1)*(9*lambda1105^2 - 1)^3));
x3315=1/8*(2- (3*(-(1/boldJ3315))^(2/3))/(-1 + sqrt((-1 + boldJ3315)/boldJ3315))^(1/3) + 3*((1- sqrt((-1 + boldJ3315)/boldJ3315))/boldJ3315)^(1/3));
lambdaast3315=sqrt(1-sqrt(1-x3315))/sqrt(2); 
lambdaast13260=(1-sqrt(1-lambdaast3315^2))/(1+sqrt(1-lambdaast3315^2)); 
x13260=4*(lambdaast13260^2-lambdaast13260^4); 
z13260=-27*x13260/(1-4*x13260)^3; 
t3315 = 1095255033002752301233099478037584/ 2050242335692983321671746996556833 + 1006588064225996719872149534306400/ 34854119706780716468419698941466161*sqrt(17)*sqrt(5) + 692779168175128551453280427070000/ 34854119706780716468419698941466161*sqrt(17) - 136434536163779492503565618457696/ 2050242335692983321671746996556833*sqrt(5) + 400179322879781860521299209248000/ 26653150364008783181732710955238829*sqrt(13) + 1077564413015882021519209726762688/ 453103556188149314089456086239060093*sqrt(13)*sqrt(17)*sqrt(5) + 120226784218523863048087030809600/ 64729079455449902012779440891294299*sqrt(17)*sqrt(13) + 239369594240980944219359445009600/ 26653150364008783181732710955238829*sqrt(13)*sqrt(5); 
alpha3315 = (1/2*sqrt(1105/3)*sqrt(1- boldJ3315)*(1-t3315)*2*(1-4*x3315)^(3/2)-(4*x3315-1 +sqrt(1 - x3315))*sqrt(3315))/(2*(1-4*x3315));
alpha13260=(4*alpha3315-2*sqrt(3315)*lambdaast3315^2)/(1+ sqrt(1-lambdaast3315^2))^2;
b13260=((8*x13260+1)*sqrt(1-x13260)*sqrt(13260))/(1-4*x13260)^(3/2);
a13260=(2*(1-4*x13260)*alpha13260+(4*x13260-1+ sqrt(1 - x13260))*sqrt(13260))/(2*(1-4*x13260)^(3/2));

print("Digits per iteration")
print(log(-1/z13260)/log(10));

print("Digits from one iteration")
print(sum(n=0,0,prod(i=0,n-1,1/2+i)*prod(i=0,n-1,1/6+i)*prod(i=0,n-1,5/6+ i)/(prod(i=0,n-1,1+i))^3*z13260^n*(a13260+b13260*n)))