--Script that enumerates according to a condition
--Import table in: https://holbertonintranet.s3.amazonaws.com/uploads/misc/2020/6/ab2979f058de215f0f2ae5b052739e76d3c02ac5.zip?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220720%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220720T175848Z&X-Amz-Expires=345600&X-Amz-SignedHeaders=host&X-Amz-Signature=e23b1cb66a7c2b19c93abffe6242eef43690d965f30059f31f361fee34ca7d2a
SELECT `band_name`, IFNULL(`split`, 2022)-`formed` AS `lifespan`
FROM `metal_bands`
WHERE `style` LIKE '%Glam rock%'
ORDER BY `lifespan` DESC;
