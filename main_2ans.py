def construct_main(cmd):
    layer = 1
    html = ""
    # construct start
    html += "<!DOCTYPE html>\n" + \
            "<html>\n" + \
            "<body>\n" + \
            "<!-- " + str(layer) + " -->\n" + \
            "<section style=\"overflow-y: hidden; box-sizing: border-box; line-height: 0;\">\n"
    # construct A,B
    for index in range(2):
        html += "\t" * layer + "<!-- " + str(layer) + "-" + "abc"[index] + " = " + str(layer + 1) + " -->\n" + \
                "\t" * layer + "<section style=\"height: 0px; box-sizing: border-box;\">\n" + \
                "\t" * layer + "<img width=\"100%\" src=\"" + img_url[cmd[0]] + "\" style=\"box-sizing: border-box;\">\n" + \
                "\t" * layer + "<section style=\"overflow: hidden; box-sizing: border-box;\">\n"
        html += "\t" * (layer + 1) + "<!-- " + str(layer + 1) + "-" + "abc"[index] + " = " + str(layer + 2) + " -->\n"
        html += construct_layer(cmd[index + 1], layer + 1, index)
        html += "\t" * layer + "</section>\n" + \
                "\t" * layer + "</section>\n"
    # construct end
    html += "\t" * layer + "<!-- " + str(layer) + "-space -->\n" + \
            "\t" * layer + "<section style=\"pointer-events: none; box-sizing: border-box;\">\n" + \
            "\t" * layer + "<svg viewBox=\"0 0 100 400\" xmlns=\"http://www.w3.org/2000/svg\"\n" + \
            "\t" * layer + "style=\"pointer-events: none; visibility: hidden; box-sizing: border-box;\"></svg>\n" + \
            "\t" * layer + "</section>\n" + \
            "</section>\n" + \
            "</body>\n" + \
            "</html>\n"
    return html


def construct_layer(cmd, layer, order):
    html = ""
    if len(cmd) <= 2:
        html += "\t" * layer + "<section style =\"height: 0px; box-sizing: border-box; pointer-events: none;\">\n"
        html += "\t" * layer + "<img width=\"100%\" style=\"pointer-events: none;\" src=\"" + img_url[cmd[0]] + "\" style=\"box-sizing: border-box;\">\n"
        html += "\t" * layer + "<img width=\"100%\" src=\"" + img_url[cmd[1]] + "\" style=\"box-sizing: border-box;\">\n"
        html += "\t" * layer + "</section>\n"
    else:
        for index in range(2):
            html += "\t" * layer + "<section style =\"height: 0px; box-sizing: border-box; pointer-events: none;\">\n"
            html += "\t" * layer + "<img width=\"100%\" style=\"pointer-events: none;\" src=\"" + img_url[cmd[0]] + "\" style=\"box-sizing: border-box;\">\n"
            html += "\t" * layer + "<img width=\"100%\" src=\"" + img_url[cmd[1]] + "\" style=\"box-sizing: border-box;\">\n"

            html += "\t" * layer + "<section style=\"overflow: hidden; box-sizing: border-box;\">\n"
            html += "\t" * (layer + 1) + "<!-- " + str(layer + 1) + "-" + "abc"[index] + " = " + str(layer + 2) + " -->\n"
            html += construct_layer(cmd[index + 2], layer + 1, index)
            html += "\t" * layer + "</section>\n"
            html += "\t" * layer + "</section>\n"
    html += "\t" * layer + "<!-- " + str(layer) + "-space -->\n" + \
            "\t" * layer + "<svg xmlns=\"http://www.w3.org/2000/svg\" style=\"display: block; pointer-events: none;  max-width: none !important; box-sizing: border-box;\" viewBox=\"0 0 100 50\">\n" + \
            "\t" * layer + "<foreignObject x=\"" + str(50 * order) + "%\" y=\"0%\" width=\"50%\" height=\"100%\">\n" + \
            "\t" * layer + "<svg viewBox=\"0 0 50 50\" xmlns=\"http://www.w3.org/2000/svg\"\n" + \
            "\t" * layer + " style=\"background-size: cover; background-image: url(&quot;"+img_url["ABC"[order]]+"&quot;); pointer-events: visible;box-sizing: border-box;\">\n" + \
            "\t" * layer + "<set attributeName=\"visibility\" from=\"visible\" to=\"hidden\" begin=\"click\"></set>\n" + \
            "\t" * layer + "</svg>\n" + \
            "\t" * layer + "</foreignObject>\n" + \
            "\t" * layer + "<animate fill=\"freeze\" attributeName=\"width\" begin=\"click\" dur=\"0.1\" from=\"100%\" to=\"800%\"></animate>\n" + \
            "\t" * layer + "</svg>\n"
    return html


my_cmd = ["1",
          ["ABC", "2", ["ABC", "3"], ["ABC", "3"]],
          ["ABC", "2", ["ABC", "3"], ["ABC", "3"]],
          ["ABC", "2", ["ABC", "3"], ["ABC", "3"]]
          ]
img_url = {}
img_url["1"] = "https://mmbiz.qpic.cn/mmbiz_png/45W5S991PV1aYwQBs5VicpxHzt2f3xTm7NqbOH8s3vThUiaj8ncCDl9Ty2LsBPHtPbjW3PCQGFEV1YBf13zqOKEg/0?wx_fmt=png"
img_url["ABC"] = "https://mmbiz.qpic.cn/mmbiz_png/45W5S991PV1aYwQBs5VicpxHzt2f3xTm77wvlPrDmbp5f2euHkibFPia3ZDMjzy3mp2H5vAZq3yweicNwFFb5oM48A/0?wx_fmt=png"
img_url["2"] = "https://mmbiz.qpic.cn/mmbiz_png/45W5S991PV1aYwQBs5VicpxHzt2f3xTm7hHgjtEGTayDg8eWqcQ9ic0iajibgNprHHtw07ibDLtLPyhuvAkCVc7uPvw/0?wx_fmt=png"
img_url["3"] = "https://mmbiz.qpic.cn/mmbiz_png/45W5S991PV1aYwQBs5VicpxHzt2f3xTm7nKOicmsI0gyj3Rswj8miaKmzgtib5PzPFNVFZgt6gB91EbNmv3tBuneTw/0?wx_fmt=png"

img_url["A"] = "https://mmbiz.qpic.cn/mmbiz_png/45W5S991PV1aYwQBs5VicpxHzt2f3xTm7N2LaXcae4qZtC8KuEyqTUrVibmsfZ44PPTUxag18bXyB2ibHkrN7UFNw/0?wx_fmt=png"
img_url["B"] = "https://mmbiz.qpic.cn/mmbiz_png/45W5S991PV1aYwQBs5VicpxHzt2f3xTm7MWzjrOojBkiccau1P30VghJibm5Ar9MzYzGAcJCDcEazbHRPsfhtJDNQ/0?wx_fmt=png"
img_url["C"] = "https://mmbiz.qpic.cn/mmbiz_png/45W5S991PV1aYwQBs5VicpxHzt2f3xTm7N2LaXcae4qZtC8KuEyqTUrVibmsfZ44PPTUxag18bXyB2ibHkrN7UFNw/0?wx_fmt=png"

with open('./test.html', 'w+') as f:
    print(construct_main(my_cmd), file=f)
