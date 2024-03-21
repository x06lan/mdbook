# dot process

tags: `graphviz`

```dot process
digraph hierarchy {
                nodesep=0.5
                node [color=Red,fontname=Courier,shape=box]
                edge [color=Blue, style=dashed]

                {"15 10 11 12 1 2 3"}

                "15 10 11 12 1 2 3"->{"4"}
                "4"->{"5 6"}[label="true"]
                "4"->{"8"}[label="false"]
                {"5 6"}->7[label=ture]
                {"5 6"}->{4}[label="false"]
                7->{4}
                {8}->{"12 13"}


}
```

```dot process
digraph hierarchy {
                nodesep=0.5
                node [color=Red,fontname=Courier,shape=box]
                edge [color=Blue, style=dashed]

                {"17 12 13 1 2 3"}

                "17 12 13 1 2 3"->{"4"}

}
```

```dot process
digraph structs{
    node[shape=record]
    start [label="{<f0> start}" shape=Mrecord]
    cpu [label="{<f0> cpu| UV | vertex |face }" shape=Mrecord]
	bind [label="{<f0> gpu ram  }" shape=Mrecord]
	draw [label="{<f0> drawcall| gpu start render }" shape=Mrecord]
	vertex [label="{<f0>vertex shader | vertex transform| normal transform|MVP |displacement}" shape=Mrecord]
	draw [label="{<f0> drawcall| gpu start render }" shape=Mrecord]
	geo [label="{<f0>geometry shader |normal visualization |TBN normal map}" shape=Mrecord]
	rez [label="{<f0>rasterization }" shape=Mrecord]
	culling [label="{<f0>culling |remove unneed vertex }" shape=Mrecord]
	frag [label="{<f0>fragment shader|lighting | color|shadow  }" shape=Mrecord]
	framebuffer [label="{<f0>frame buffer | postprocess}" shape=Mrecord]


    start:f0 -> cpu:f0
	cpu->bind[label = "vertex data"]
    bind:f0 -> draw
	draw->vertex
	vertex->geo
    geo->culling
    culling->rez
    rez->frag
	frag->framebuffer

    // struct1:f0 -> struct3:f1;

}
```

```dot process
digraph google{
    // layout=neato;
    // layout=circo;
	// layout=twopi;
    fontname="Helvetica,Arial,sans-serif"
    fontcolor=white
    // bgcolor="black"
    // bgcolor="transparent"
    node[shape=circle,style=filled,color=white,colorscheme=ylgnbu7]
    edge[color=white,dir="both"]
    label="node tree 001 to 101 "
	"000"
	"001"
	"010"
	"011"
	"100"
	"101"
	"110"
	"111"
	"000"
}
```

```dot process
digraph google{
    // layout=neato;
    layout=circo;
	// layout=twopi;
    fontname="Helvetica,Arial,sans-serif"
    fontcolor=white
    // bgcolor="black"
    bgcolor="transparent"
    node[shape=circle,style=filled,color=white,colorscheme=ylgnbu7]
    edge[color=white,dir="both"]
    label="nodes with index"
	// "000"->"001"->"010"->"011"->"100"->"101"->"110"->"111"->"000"
	"000"
	"001"
	"010"
	"011"
	"100"
	"101"
	"110"
	"111"
}
```

```dot process
digraph google{
    // layout=neato;
    layout=circo;
	// layout=twopi;
    fontname="Helvetica,Arial,sans-serif"
    fontcolor=white
    bgcolor="black"
    // bgcolor="transparent"
    node[shape=circle,style=filled,color=white,colorscheme=ylgnbu7]
    edge[color=white,dir="both"]
    label="mesh network"
	// "000"->"001"->"010"->"011"->"100"->"101"->"110"->"111"->"000"
	"000"->"001" "000"->"010" "000"->"011"  "000"->"100"  "000"->"101"  "000"->"110"  "000"->"111"
	"001"->"010" "001"->"011" "001"->"100"  "001"->"101"  "001"->"110"  "001"->"111"
	"010"->"011" "010"->"100" "010"->"101"  "010"->"110"  "010"->"111"
	"011"->"100" "011"->"101" "011"->"110"  "011"->"111"
	"100"->"101" "100"->"110" "100"->"111"
	"101"->"110" "101"->"111"
	 "110"->"111"

	// mode="ipsep"
	// "000"[root=true]
    // "010"-> "101" [constraint=false color=red,mode="ipsep"];


}
```

```dot process
digraph tracker{
    // layout=neato;
    // layout=circo;
	// layout=twopi;
    fontname="Helvetica,Arial,sans-serif"
    fontcolor=white
    bgcolor="black"
    // bgcolor="transparent"
    node[shape=circle,style=filled,color=white,colorscheme=ylgnbu7,fontsize=15]
    edge[color=white,penwidth=2 ,minlen=3]
    label="tracker server"
	// "000"->"001"->"010"->"011"->"100"->"101"->"110"->"111"->"000"
	"tracker server"[shape=box,fontsize=20,color="#00ff00"]

	"tracker server"->"client11"
	"client11"->"tracker server"
    "client11"-> "You" [constraint=false,color=green ,minlen=3,dir="both"];

	"tracker server"->"You"
	"You"->"tracker server"

	"tracker server"->"client10"
	"client10"->"tracker server"
    "client10"-> "You" [constraint=false,color=green ,minlen=3,dir="both"];

}
```

```dot process
digraph google{
    // layout=neato;
    layout=circo;
	// layout=twopi;
    fontname="Helvetica,Arial,sans-serif"
    fontcolor=white
    bgcolor="black"
    // bgcolor="transparent"
    node[shape=circle,style=filled,color=white,colorscheme=ylgnbu7]
    edge[color=white]
    label="real world"
	// "000"->"001"->"010"->"011"->"100"->"101"->"110"->"111"->"000"
	"000"
	"001"->"010"[color=red]
    "001"->"011"[color=red]
    "001"->"110"[color=red]
    "001"->"100"[color=red]
    "001"->"111"[color=red]
	"010"
	"011"
	"100"->"101"[color=green]
    "100"->"111"[color=green]
    "100"->"110"[color=green]
    "100"->"001"[color=green]
    "100"->"010"[color=green]
    "100"->"011"[color=green]
	"101"
	"110"->"111"[color=skyblue]
    "110"->"100"[color=skyblue]
    "110"->"011"[color=skyblue]
    "110"->"010"[color=skyblue]
    "110"->"001"[color=skyblue]
    "110"->"000"[color=skyblue]
	"111"
	// "111"->"101"
	"000"

}
```

```dot process
digraph structs{
    fontcolor=white
    bgcolor="black"
    // bgcolor="transparent"
    node[shape=record,style=filled,color=black
    fillcolor=white]
	edge[dir="back",color=green]
    start [label="{You|{<f0>⠀⠀⠀|001|010}|{011|100|<f1>⠀⠀}|{110|<f2>⠀⠀|___}}" shape=Mrecord]
    n1 [label="{N1|{<f0>000|⠀⠀|010}|{011|100|⠀⠀}|{⠀⠀|111|___}}" shape=Mrecord]
    n2 [label="{N2|{⠀⠀|001|⠀⠀}|{⠀⠀|⠀⠀|<f1>101}|{110|111|___}}" shape=Mrecord]
    n3 [label="{N3|{⠀⠀|001|010}|{⠀⠀|100|101}|{110|<f2>111|___}}" shape=Mrecord]

    start:f0 -> n1:f0
    start:f1 -> n2:f1
    start:f2 -> n3:f2
}
```

```dot process
digraph google{
    // layout=neato;
    layout=circo;
	// layout=twopi;
    fontname="Helvetica,Arial,sans-serif"
    fontcolor=white
    bgcolor="black"
    // bgcolor="transparent"
    node[shape=circle,style=filled,color=white,colorscheme=ylgnbu7]
    edge[color=white]
    label="100 to 101"
	// "000"->"001"->"010"->"011"->"100"->"101"->"110"->"111"->"000"
	"000"
	"001"->"010"
    "001"->"011"
    "001"->"110"
    "001"->"100"
    "001"->"111"
	"010"
	"011"
	"100"->"101"[color=blue]
    "100"->"111"[color=red]
    "100"->"110"[color=red]
    "100"->"001"[color=green]
    "100"->"010"[color=green]
    "100"->"011"[color=green]
	"101"
	"110"->"111"
    "110"->"100"
    "110"->"011"
    "110"->"010"
    "110"->"001"
    "110"->"000"
	"111"
	"000"
}
```

```dot process
digraph google{
node[shape=record]
  label="node tree"
   nnnn [label="***"] ;
   nnnn ->"1**" ;
   "1**"->"11*";
   "11*"->"111";
   "11*"->"110";
   "1**"->"10*";
   "10*"->"101";
   "10*"->"100";


	nnnn ->"0**";
   "0**"->"01*";
   "0**"->"00*";
   "01*"->"011";
   "01*"->"010";
   "00*"->"001";
   "00*"->"000";
}
```

```dot process
digraph google{
    fontcolor=white
  fontname="Helvetica,Arial,sans-serif"

    // bgcolor="transparent"
    bgcolor="black"
    node[shape=record,style=filled,color=white]
    edge[color=white]
    	subgraph cluster_3 {

		"1**"
		"11*"
		"111"
		"110"
		"10*"
		"101"
		"100"
		label = "k-bucket 2";
		color=green
	}
		subgraph cluster_2 {
		"0**"
		"01*"
		"011"
		"010"

		label = "k-bucket 1";
		color=red
	}
       subgraph cluster_1 {

		"00*"
		"000"
		label = "k-bucket 0";
		color=blue
	}

  label="node tree 001 to 101 "
   nnnn [label="***"] ;
   nnnn ->"1**" ;
   "1**"->"11*";
   "11*"->"111";
   "11*"->"110";
   "1**"->"10*";
   "10*"->"101";
   "10*"->"100";
	nnnn ->"0**";
   "0**"->"01*";
   "0**"->"00*";
   "01*"->"011";
   "01*"->"010";
   "00*"->"001";
   "00*"->"000";
}

```

```dot process
digraph google{
    fontcolor=white
    fontname="Helvetica,Arial,sans-serif"

    // bgcolor="transparent"
    bgcolor="black"

    node[shape=record,style=filled,color=white,colorscheme=ylgnbu7]
    edge[color=white]
    subgraph cluster_3 {
		"1**"
		"11*"
		"111"
		"110"
		"10*"
		"101"
		"100"
		label = "k-bucket 2(001 xor 101 =100)";
		color=green
	}
  label="node tree 001 to 101 "
   nnnn [label="***"]
   nnnn ->"1**";
   "1**"->"11*";
   "11*"->"111";
   "11*"->"110";
   "1**"->"10*";
   "10*"->"101";
   "10*"->"100";
   nnnn ->"0**";
   "0**"->"01*";
   "0**"->"00*";
   "01*"->"011";
   "01*"->"010";
   "00*"->"001";
   "00*"->"000";

    "001"-> "101" [constraint=false color=red];
    // "001" "111" rank=same ;
   // "001"->"111"[rank=same];

}

```
