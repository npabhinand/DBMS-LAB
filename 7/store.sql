CREATE DEFINER=`root`@`localhost` PROCEDURE `insert_product`(IN barcode int,IN product_name varchar(20),IN price int,IN quantity int)
BEGIN
	if(price>0 and quantity>=0) then
    insert into product values(barcode,product_name,price,quantity);
    end if;
END