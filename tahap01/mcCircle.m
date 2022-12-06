function [map,circleArea,circlePercent,pixIn,pixPercent] = mcCircle(width,height,a,b,r,mcIteration)

map = zeros(width,height);
mapArea = width*height;
mcColor = 100;

% Create a white-filled circle
mapCount = 0;
for y = 1:height
    for x = 1:width
        if abs((x-a)^2 + (y-b)^2) <= r^2
            map(y,x) = 255;
            mapCount = mapCount+1;
        end
    end
end

% MC Calculation
mc = 1;
while mc <= mcIteration
    %fprintf('Iteration no. %d\n',mc)
    i = randi(height);
    j = randi(width);
    if map(i,j) == mcColor
        while map(i,j) == mcColor
            i = randi(height);
            j = randi(width);
        end
        map(i,j) = mcColor;
    else
        map(i,j) = mcColor;
    end
    mc = mc+1;
end

pixIn = 0;
% Calculate the results
for y = 1:height
    for x = 1:width
        if abs((x-a)^2 + (y-b)^2) <= r^2 && map(y,x) == mcColor
            pixIn = pixIn+1;
        end
    end
end

circleArea = pi*(r^2);
circlePercent = (circleArea/mapArea)*100;
pixPercent = (pixIn/mcIteration)*100;