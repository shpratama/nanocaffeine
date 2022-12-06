clear
clc

width = 400;
height = 400;
a = 200;
b = 200;
r = 200;

iterStart = 100;
iterStep = 100;
iterEnd = 1000;

iterMarker = 10000;

if iterEnd > (pi*(r^2))
    fprintf('Sampling iteration is more than the circle area! Should be lower than %.0f.\n',pi*(r^2))
    return
end

i=1;

for iter=iterStart:iterStep:iterEnd
    [map,circleArea,circlePercent,pixIn,pixPercent] = mcCircle(width,height,a,b,r,iter);
    totalPercent(i) = pixPercent;
    i = i+1;
    if mod(iter,iterMarker) == 0
        fprintf('Iteration to %d\n',iter)
    end
end

xAxis = iterStart:iterStep:iterEnd;
yLine(1:numel(xAxis)) = circlePercent;

figure(1);
plot(xAxis,yLine,xAxis,totalPercent)
xlabel('Sampling Frequency')
ylabel('Circle Percentage')
legend('Analytic Calc.','Monte Carlo Calc.')
ylim([min(totalPercent)-(0.1*min(totalPercent)) max(totalPercent)+(0.1*max(totalPercent))])

