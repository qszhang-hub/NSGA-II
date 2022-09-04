% 循环读取结果并计算hv值
clc;clear;close all
indexs = [1,2,3,5,7];  % 题号列表
HVs = zeros(size(indexs, 2), 20);  % 存放所有hv值
for i = 1:size(indexs, 2)
    index = indexs(i);  % 题号
    for j=1:20  % 轮数
        load(['Result\NSGA2_Pop_' num2str(index) '_' num2str(j) '.mat']);
        HV_Score = HV(Pop, index);
        HVs(i, j) = HV_Score;
        fprintf('NSGA2 for RWCMOP %d run = %d HV = %f\n', index, j, HV_Score);
    end
    fprintf('\nNSGA2 for RWCMOP %d Best HV = %f\n', index, max(HVs(i, :)));
    fprintf('NSGA2 for RWCMOP %d Mean HV = %f\n\n', index, mean(HVs(i, :)));
end
HVs