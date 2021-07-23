# Python program to create custom avatars

# importing the require package
import py_avataaars as pa
import itertools


# assigning various parameters to our avatar
avatar = pa.PyAvataaar(style=pa.AvatarStyle.CIRCLE,
                    skin_color=pa.SkinColor.LIGHT,
                    hair_color=pa.HairColor.AUBURN,
                    facial_hair_type=pa.FacialHairType.MOUSTACHE_MAGNUM,
                    top_type=pa.TopType.SHORT_HAIR_SHAGGY_MULLET,
                    mouth_type=pa.MouthType.SCREAM_OPEN,
                    eye_type=pa.EyesType.SQUINT,
                    eyebrow_type=pa.EyebrowType.RAISED_EXCITED_NATURAL,
                    nose_type=pa.NoseType.DEFAULT,
                    accessories_type=pa.AccessoriesType.PRESCRIPTION_02,
                    clothe_type=pa.ClotheType.HOODIE,
                    clothe_graphic_type=pa.ClotheGraphicType.BAT,)





stylesObj = {};
styleTypesArray = [pa.AvatarStyle, pa.SkinColor, pa.HairColor, pa.FacialHairType];    
styleTypesNamesArray = ["style", "skin_color", "hair_color", "facial_hair_type"];


# stylesObj[styleTypesNamesArray[2]] = styleTypesArray[2](9).name;
# stylesObj['hair_color'] = pa.HairColor.SILVER_GRAY;
# print("old")
# print (stylesObj);

stylesObj[styleTypesNamesArray[2]] = styleTypesArray[2](9);
print("new")
print (stylesObj);
avatar = pa.PyAvataaar(**stylesObj)
avatar.render_png_file("output_images/TESTING.png")
avatar.render_svg_file("output_images/TESTING.svg")


def setStyleOfImageForOneType(stylesObj, styleTypeIndex, actualStyleIndex, stylesMap):

    styleTypesArray = [pa.AvatarStyle, pa.SkinColor, pa.HairColor, pa.TopType, pa.FacialHairType, pa.ClotheType, pa.ClotheGraphicType, pa.Color, pa.MouthType, pa.NoseType, pa.EyesType, pa.EyebrowType, pa.AccessoriesType]; 
    styleTypesNamesArray = ["style", "skin_color", "hair_color", "top_type", "facial_hair_type", "clothe_type", "clothe_graphic_type", "background_color", "mouth_type", "nose_type", "eye_type", "eyebrow_type", "accessories_type"];
    # stylesObj[styleTypesArray[styleTypeIndex]] = stylesMap[styleTypeIndex][actualStyleIndex]
    stylesObj[styleTypesNamesArray[styleTypeIndex]] = styleTypesArray[styleTypeIndex](actualStyleIndex);
    # stylesObj[styleTypesArray[styleTypeIndex]] = stylesMap[styleTypeIndex][actualStyleIndex]

    return stylesObj;


# list of all base styles
# create an array for each type of attribute with all enums inside.
# filter out internal attributes and functions since we only need user defined attributes

stylesMap = [];

#case 1
baseStyle = [a for a in dir(pa.AvatarStyle) if not a.startswith('__') and not callable(getattr(pa.AvatarStyle, a))]
stylesMap.append(baseStyle);

#case 2
skinColor = [a for a in dir(pa.SkinColor) if not a.startswith('__') and not callable(getattr(pa.SkinColor, a))]
stylesMap.append(skinColor); 

#case 3
hairColor = [a for a in dir(pa.HairColor) if not a.startswith('__') and not callable(getattr(pa.HairColor, a))]
stylesMap.append(hairColor); 

# case 4
TopType = [a for a in dir(pa.TopType) if not a.startswith('__') and not callable(getattr(pa.TopType, a))]
stylesMap.append(TopType); 

# case 5
facialHairType = [a for a in dir(pa.FacialHairType) if not a.startswith('__') and not callable(getattr(pa.FacialHairType, a))]
stylesMap.append(facialHairType); 


# case 6
ClotheType = [a for a in dir(pa.ClotheType) if not a.startswith('__') and not callable(getattr(pa.ClotheType, a))]
stylesMap.append(ClotheType); 

# case 7
ClotheGraphicType = [a for a in dir(pa.ClotheGraphicType) if not a.startswith('__') and not callable(getattr(pa.ClotheGraphicType, a))]
stylesMap.append(ClotheGraphicType); 

# case 8
Color = [a for a in dir(pa.Color) if not a.startswith('__') and not callable(getattr(pa.Color, a))]
stylesMap.append(Color); 

# case 8
MouthType = [a for a in dir(pa.MouthType) if not a.startswith('__') and not callable(getattr(pa.MouthType, a))]
stylesMap.append(MouthType); 

# case 8
NoseType = [a for a in dir(pa.NoseType) if not a.startswith('__') and not callable(getattr(pa.NoseType, a))]
stylesMap.append(NoseType); 

# case 9
EyesType = [a for a in dir(pa.EyesType) if not a.startswith('__') and not callable(getattr(pa.EyesType, a))]
stylesMap.append(EyesType); 

# case 10
EyebrowType = [a for a in dir(pa.EyebrowType) if not a.startswith('__') and not callable(getattr(pa.EyebrowType, a))]
stylesMap.append(EyebrowType); 

# case 11
AccessoriesType = [a for a in dir(pa.AccessoriesType) if not a.startswith('__') and not callable(getattr(pa.AccessoriesType, a))]
stylesMap.append(AccessoriesType); 

def returnListOfAllcombinationsOfAcertainSize(size):

    k=0;

    #array with readable names

    readableListOfAllcombinationsOfAcertainSize = [];
    listOfAllcombinationsOfAcertainSize = [];

    #array with actual indices 

    #print all combinations of a certain size 
    for comb in itertools.combinations(stylesMap, size):
        # print (comb);

        # print("START find indices of selected sets");
        indicesOfSelectedComb = [];
        #tuple of size X
        for m in comb:
            indicesOfSelectedComb.append(stylesMap.index(m));

        # print(indicesOfSelectedComb);
        # print("END find indices of selected sets");

        for finalTuple in itertools.product(*comb):
             # ex: finalTuple = ('BLACK', 'SILVER_GRAY')
            k = k+1;
            # print(k)
            #print(finalTuple)

            #add to readablelist
            readableListOfAllcombinationsOfAcertainSize.append(finalTuple);

            n = 0
            finalTupleLoc = []; 
            # example
            # ('TRANSPARENT', 'YELLOW', 'SILVER_GRAY')
            # [(0,1) , (1,6) , (2,9)]
            #  (0,1) is singleAtttributeLoc
                

            for singleAtttribute in finalTuple:
                # get index of singleAtttribute ex: SILVER_GRAY is 9
                y = stylesMap[indicesOfSelectedComb[n]].index(singleAtttribute);
                x = indicesOfSelectedComb[n];
                #find x and y of this single attribute in stylesMap
                singleAtttributeLoc =  (x,y);
                n = n+1;
                finalTupleLoc.append(singleAtttributeLoc);

            listOfAllcombinationsOfAcertainSize.append(finalTupleLoc);

    return listOfAllcombinationsOfAcertainSize;

def createImagesOfFromList(listOfAllcombinations):

    imageNum = 0
    for allStyles in listOfAllcombinations:

        stylesObj = {};
        imageNum = imageNum+1

        for eachStyle in allStyles:
            #pick the styleType and apply for eachStyle
            styleTypeIndex = eachStyle[0];
            actualStyleIndex = eachStyle[1];
            stylesObj = setStyleOfImageForOneType(stylesObj, styleTypeIndex, actualStyleIndex, stylesMap)

        print(imageNum);
        print(stylesObj);

        avatar = pa.PyAvataaar(**stylesObj)
        avatar.render_png_file("output_images/AVATAR_" + str(imageNum) + ".png")        

def giveFinalAndAllCombinationsGivenNumOfAttributes(numOfAttributes):

    finalCombinations = [];
    for x in range(numOfAttributes):
        finalCombinations = finalCombinations + returnListOfAllcombinationsOfAcertainSize(x+1)
    return finalCombinations;

print(len(returnListOfAllcombinationsOfAcertainSize(1)));
print(len(returnListOfAllcombinationsOfAcertainSize(2)));
# print(len(returnListOfAllcombinationsOfAcertainSize(3)));
# print(len(returnListOfAllcombinationsOfAcertainSize(4)));
# print(len(returnListOfAllcombinationsOfAcertainSize(5)));
# print(len(returnListOfAllcombinationsOfAcertainSize(6)));
# print(len(returnListOfAllcombinationsOfAcertainSize(7)));
# print(len(returnListOfAllcombinationsOfAcertainSize(8)));
# print(len(returnListOfAllcombinationsOfAcertainSize(9)));
# print(len(returnListOfAllcombinationsOfAcertainSize(10)));

#USE this if you want combinations involving all attributes upto size X;
# that is Nc1 + Nc2 + Nc3 + ..... + NcX
allCombinationsUptoSizeX = giveFinalAndAllCombinationsGivenNumOfAttributes(1);

#USE this if you want combinations involving all attributes of EXACT size X;
# that is NcX
allCombinationsOfSizeX = returnListOfAllcombinationsOfAcertainSize(1);

# print(len(giveFinalAndAllCombinationsGivenNumOfAttributes(1)));

# createImagesOfFromList(allCombinationsOfSizeX);