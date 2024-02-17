import os,sys

path = os.getcwd()+"\\"

files = os.listdir(path)
dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(dir)

args = sys.argv
dir_name = ""

# if 2 <= len(args):
#     dir_name = args[1]
# else:
print("ファイル名 : ")
dir_name = input()

os.rename(path + dir[0], path + dir_name)

files = os.listdir(path + dir_name +"/images")
print(len(files))
page = len(files)
next = "\"../" + str(int(dir_name)+1) + "/index.html\""
prev = "\"../" + str(int(dir_name)-1) + "/index.html\""

print(path + dir_name + "/index.html")
f = open(path + dir_name + "/index.html", "w", encoding='utf-8')
f.write("""
<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <title></title>
    <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1, maximum-scale=1">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.css" rel="stylesheet">
    <link href="../../images/style.css" rel="stylesheet">
    <link href="../../comi_style.css" rel="stylesheet">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script>

        /** 入力ここから **/
        var page = """
        +str(page) + """; //ページ数
        var imgtype = "jpeg"; //画像の拡張子
        var display = 0; //左ページ始まりは「0」、右ページ始まりは「1」
        /* *ここまで **/
        
        $(function(){
            for(var i=3; i<=page; i++){
                $('#last_page').before('<div class="c_i"><div><img data-lazy="'+'./images/' + ('00000'+ i).slice(-5) + '.' + imgtype + '" src="../../images/load.gif"></div></div>'); 
            }
            
            /**長すぎるからh1の方のタイトル改行したいって時var/コメントアウト解除して編集**/
            //$("h1").html("サンプル<br>サンプル");
             
        });
    </script>
</head>
<body>
    <!--漫画表示ゾーンここから-->
    <div class="slider" dir="rtl">
        <div id="first_page"></div>
        <div id="last_page">
            <div class="last_page_in" dir="ltr">
                <div>
                    <!--最終ページフリー追加ゾーンここから-->

                    

                    <!--最終ページフリー追加ゾーンここまで-->
                </div>
                <h1></h1>
                <!--最終ページにボタンを追加する場合は以下をコメントアウト解除して編集-->
                <p>
                    <a class="button" href="""+ next + """>次の話へ</a>
                    <a class="button" href="""+ prev + """>前の話へ</a>
                </p>
                <p>
                    <input type="button" value="もう一度読む" class="button b_button">
                    <input type="button" value="サイトへ戻る" class="button o_button orange">
                </p>
            </div>
        </div>
    </div>
    <!--漫画表示ゾーンここまで-->
    
    <!--メニューここから-->
    <div class="menu_box">
        <div class="menu_button">menu</div>
        <div class="menu_show">    
            <h1></h1>
            <!--メニューにボタンを追加する場合は以下をコメントアウト解除して編集-->
            <p>
                <a class="button" href="""+ next + """>次の話へ</a>
                <a class="button" href="""+ prev + """>前の話へ</a>
            </p>
            <p>
                <input type="button" value="操作ヘルプ" class="button p_button">
                <input type="button" value="全画面表示" class="button g_button sp_none">
                <input type="button" value="拡大モード" class="button z_button">
                <input type="button" value="サイトへ戻る" class="button o_button orange">
            </p>
            <div class="slick-counter"><span class="current"></span> / <span class="total"></span></div>
            <div class="dots" dir="rtl"></div>
            <div class="menu_button close">close</div>
        </div>
    </div>
    <!--メニューここまで-->
    
    <!--操作ヘルプここから-->
    <div class="help">
        <div class="help_in">
            <div class="help_img"><img src="../../images/help.png" width="300"></div>
            <p>【画面操作】</p>
            <!--class="sp_none"でPC以外だと非表示・class="pc_none"でPCだと非表示-->
            <ul class="pc_none">
                <li>&#9312;中央ダブルタップ<span>……拡大モード</span></li>
                <li>&#9312;中央フリック<span>……次のページ・前のページ</span></li>
                <li>&#9313;両端タップ<span>……次のページ・前のページ</span></li>
                <li>&#9314;ページャータップ<span>……ページ移動</span></li>
            </ul>
            <ul class="sp_none">
                <li>&#9312;中央スライド<span>……次のページ・前のページ</span></li>
                <li>&#9313;両端クリック<span>……次のページ・前のページ</span></li>
                <li>&#9314;ページャークリック<span>……ページ移動</span></li>
            </ul>
            <p class="sp_none">【キーボード操作】</p>
            <ul class="sp_none">
                <li>←キー……次のページ</li>
                <li>→キー……前のページ</li>
                <li>↓キー……メニュー表示</li>
                <li>↑キー……拡大モード</li>
                <li>F11キー……全画面表示</li>
            </ul>
        </div>
    </div>
    <!--操作ヘルプここまで-->
    
    <!--拡大モードここから-->
    <div class="zoomwrap"></div>
    <div class="zoom_reset z_button">
        <div class="zr_in">拡大モードを解除</div>
    </div>
    <!--拡大モードここまで-->
    
    <script src="https://cdnjs.cloudflare.com/ajax/libs/slick-carousel/1.9.0/slick.min.js"></script>
    <script src="../../comic.js"></script>
</body>
</html>
"""
)

f.close()