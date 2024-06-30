import cv2

def ocrText(model, reader):
    puzzle = []
    words = []
    
    img_path = 'output/puzzle.jpg'
    result = model.ocr(img_path, cls=True)
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            singleLine = list(line[1][0])
            puzzle.append(singleLine)
    
    img_path = 'words/words.jpg'
    words = reader.readtext(img_path, detail=0) 


    return puzzle, words
