import re

def getIds(readFrom, writeTo):
  file1 = open(readFrom + ".txt", 'r');
  contents = file1.read();
  file1.close();
  
  idRegex = re.compile(r'id=\"\w+(?:-\w+)*\"');
  idList = idRegex.findall(contents);
  
  file2 = open(writeTo + ".txt", 'w');
  hyphenatedRegex = re.compile(r'\w+(?:-\w+)*');
  disallowedIds = ["Document", "Group", "Spread", "Group_1", "Group_2", "Group_3"];
  foundIds = [];
  for i in range(len(idList)):
    item = idList[i];
    id = hyphenatedRegex.findall(item)[1];
    if (id not in disallowedIds):
      file2.write(id);
      foundIds.append(id);
      if i < len(idList) -1:
        file2.write('\n');
  file2.close();
  print('done');
  return foundIds;

def checkIds(current, original):
  def getMissing(fir, sec): 
    missing = [];
    for item in fir:
      if (item not in sec):
        missing.append(item);
    return missing;
  missingFromOriginal = getMissing(current, original);
  missingFromCurrent = getMissing(original, current);
  
  print("Missing from current: ");
  print(missingFromCurrent);
  print("Missing from original: ");
  print(missingFromOriginal);

current = getIds('current', 'currentIds');
original = getIds('original', 'originalIds');
checkIds(current, original);