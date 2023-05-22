if modes == 'keyboard'
{
    //Get the player input
    key_right = keyboard_check(ord("A"));
    key_left = -keyboard_check(ord("D"));
    key_jump = keyboard_check_pressed(ord("W"));
    
    //React to inputs
    move = key_left + key_right;
    hsp = move * movespeed;
    if (vsp < 10) vsp += grav;
    
    if (place_meeting(x,y+1,o_grassblock))
    {
        vsp = key_jump * -jumpspeed
    }
    
    // hor Col
    if (place_meeting(x+hsp,y,o_grassblock))
    {
        while(!place_meeting(x+sign(hsp),y,o_grassblock))
        {
            x += sign(hsp);
        }
        hsp = 0;
    }
    x += hsp;
    
    // vert Col
    if (place_meeting(x,y+vsp,o_grassblock))
    {
        while(!place_meeting(x,y+sign(vsp),o_grassblock))
        {
            y += sign(vsp);
        }
        vsp = 0;
    }
    y += vsp;
}
if modes == 'arrow'
{
    // Get the player input
    key_right = keyboard_check(vk_right);
    key_left = -keyboard_check(vk_left);
    key_jump = keyboard_check_pressed(vk_up);
    
    //React to inputs
    move = key_left + key_right;
    hsp = move * movespeed;
    if (vsp < 10) vsp += grav;
    
    if (place_meeting(x,y+1,o_grassblock))
    {
        vsp = key_jump * -jumpspeed
    }
    
    // hor Col
    if (place_meeting(x+hsp,y,o_grassblock))
    {
        while(!place_meeting(x+sign(hsp),y,o_grassblock))
        {
            x += sign(hsp);
        }
        hsp = 0;
    }
    x += hsp;
    
    // vert Col
    if (place_meeting(x,y+vsp,o_grassblock))
    {
        while(!place_meeting(x,y+sign(vsp),o_grassblock))
        {
            y += sign(vsp);
        }
        vsp = 0;
    }
    y += vsp;
}
