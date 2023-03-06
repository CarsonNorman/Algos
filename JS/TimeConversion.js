// Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

// Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
// - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

function timeConversion(s) {
    //check if the given time is AM or PM
    let indicator = s[8]
    //check for edge case (12:xx:xx)
    let check = ('12' === s.slice(0,2))

    if (indicator === 'P'){
        // 12:xx:xx PM is the same in 12 hour format as 24 hour 
        // so we return the given string with the PM taken off
        if(check){
            return s.slice(0,8)
        }
        //Here we add 12 to the hour portion of our string to convert to PM
        let end = s.slice(2, 8)
        return (parseInt(s.slice(0,2)) + 12) + end
    }
    else{
        //12:xx:xx AM will be converted to 00:xx:xx here
        if(check){
            let end = s.slice(2, 8)
            return '00' + end
        }
        //otherwise we simply get rid of the AM designator
        return s.slice(0,8)
    }

}