const EventEmitter = require('events');  // Step :1
var emitter = new EventEmitter();        // Step :2

// Step 1: Creating listeners / event handlers
var list1 = (message) => {       // Listener -1
    console.log('listener 1 > '+message);
};

var list2 = (message) =>{       // Listener -2
    console.log('listener 2 > '+message);
};

var list3 = (message) =>{       // Listener -3
    console.log('listener 3 > '+message);
};

var list4 = (message) =>{       // Listener -3
    console.log('listener 4 > '+message);
};

//-------------------- Step 2: Attaching the multiple listeners
emitter.once('event1', list1);
emitter.once('event1', list1);
emitter.addListener('event2',list2);
emitter.addListener('event2',list3);
emitter.on('event3',list3)
emiiter.once('event2',list2)

emitter.addListener('event4',list2)
emitter.addListener('event4',list3)
emitter.addListener('event4',list4)

console.log('total number of default listerners ' +emitter.getMaxListeners());  // 10
console.log(emitter.listenerCount());

console.log('total number of evemt2 ' + emitter.listenerCount('event2'));
console.log('total number of evemt1 ' +emitter.listenerCount('event1'));

//-------------------Step 3: emmiting the events / calling the listners
emitter.emit('event1',"1 emitted")
emitter.emit('event1',"1  again emitted")
emitter.emit('event2',"2 emitted")
emitter.emit('event3',"3 emitted")
emitter.emit('event4','4 emitted')
emitter.emit('event2',"2 once emitted")

emitter.removeListener('event2',list3)
emitter.removeAllListeners('event4')

console.log("----------------------------------")

emitter.emit('event1',"1 emitted")
emitter.emit('event1',"1  again emitted")
emitter.emit('event2',"2 emitted")
emitter.emit('event3',"3 emitted")
emitter.emit('event4','Bye')

