select info.item_id, item_name, rarity
    from item_info info
    left join item_tree tree 
    on info.item_id = tree.parent_item_id
where parent_item_id is null
order by item_id desc;