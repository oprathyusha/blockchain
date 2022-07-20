"""
Genesis block - first block
{
    index:0
    timestamp:current time
    data :
    proof: output of some mathematical computation that satisfies a condition
    previous_hash : "0"
} this is sent to hash() function -> hexadecimal value eg : 234aaa

next block
{
    index :1 
    timestamp :current time
    data :
    proof:23456
    previous_hash : "234aaa"
}->hash() ->9876eee  // if the data is changes this hash will be changed the previous_hash in the next block becomes invalid, therefore blockchain becomes invalid

next block 
{
    index :2
    timestamp :current time
    data :
    proof:23345
    previous_hash : "987eee"
}
"""
