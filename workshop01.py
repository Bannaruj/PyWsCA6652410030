def sentence_count(sentence):
    words = sentence.split()
    totalWords = len(words)
    
    uniqueWords = set(words)
    totalUnique = len(uniqueWords)
    
    duplicateWords = [word for word in uniqueWords if words.count(word) > 1]
    
    print(f"มีคำรวมทั้งหมด {totalWords} คำ")
    print(f"มีคำที่ซ้ำกันรวม {len(duplicateWords)} คำ คือ {' '.join(duplicateWords)}")
    
    for word in duplicateWords:
        count = words.count(word)
        print(f"คำว่า {word} ซ้ำกัน {count} ครั้ง")

try:
    inputSentence = input("ป้อนประโยค: ")
    sentence_count(inputSentence)
except Exception as e:
    print(f"เกิดข้อผิดพลาด: {e}")