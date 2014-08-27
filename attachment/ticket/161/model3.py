<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  
  

  
    



    <head>
    <title>
      model3.py on Ticket #161 – Attachment
     – FiPy
    </title>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!--[if IE]><script type="text/javascript">
      if (/^#__msie303:/.test(window.location.hash))
        window.location.replace(window.location.hash.replace(/^#__msie303:/, '#'));
    </script><![endif]-->
        <link rel="search" href="/fipy/search" />
        <link rel="help" href="/fipy/wiki/TracGuide" />
        <link rel="alternate" href="/fipy/raw-attachment/ticket/161/model3.py" type="application/x-python; charset=iso-8859-15" title="Original Format" />
        <link rel="up" href="/fipy/ticket/161" title="Ticket #161" />
        <link rel="start" href="/fipy/wiki" />
        <link rel="stylesheet" href="/trac_1.0_htdocs/css/trac.css" type="text/css" /><link rel="stylesheet" href="/fipy/pygments/trac.css" type="text/css" /><link rel="stylesheet" href="/trac_1.0_htdocs/css/code.css" type="text/css" />
        <link rel="shortcut icon" href="/fipy/chrome/common/trac.ico" type="image/x-icon" />
        <link rel="icon" href="/fipy/chrome/common/trac.ico" type="image/x-icon" />
      <link type="application/opensearchdescription+xml" rel="search" href="/fipy/search/opensearch" title="Search FiPy" />
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/jquery.js"></script>
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/babel.js"></script>
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/trac.js"></script>
      <script type="text/javascript" charset="utf-8" src="/trac_1.0_htdocs/js/search.js"></script>
      <script type="text/javascript" src="/trac_1.0_htdocs/js/folding.js"></script>
      <script type="text/javascript">
        jQuery(document).ready(function($) {
          $('#preview table.code').enableCollapsibleColumns($('#preview table.code thead th.content'));
        });
      </script>
        <link rel="stylesheet" type="text/css" href="/trac_1.0_htdocs//css/matdlosi.css" />
	<style type="text/css">
	body {width: 95%;}
	</style>
    </head>
    <body>
    <div id="banner">
      <div id="header">
            <div id="topLogo">
                <img src="/trac_1.0_htdocs//hdr_main.jpg" alt="Main Header" usemap="#MatDL_Banner_Narrow_Map" />
                <map name="MatDL_Banner_Narrow_Map">
                    <area shape="rect" alt="Materials Digital Library" coords="44,53,263,70" href="http://matdl.org" />
                    <area shape="rect" alt="NSDL logo" coords="675,43,740,71" href="http://nsdl.org" />
                    <area shape="rect" alt="NSF logo" coords="686,0,731,43" href="http://nsf.gov" />
                    <area shape="rect" alt="MatDL logo" coords="44,0,158,53" href="http://matdl.org" />
                </map>
                <br />
                <br />
            </div>
            <div id="projheader">
                <h1 style="margin: 0px;">
                    <img style="width: 50px;" src="/fipy/chrome/site/fipy-logo.png" alt="FiPy" />
                FiPy: A Finite Volume PDE Solver Using Python</h1>
                <a href="http://www.ctcms.nist.gov/fipy">FiPy Home</a>
            </div>
        </div>
      <form id="search" action="/fipy/search" method="get">
        <div>
          <label for="proj-search">Search:</label>
          <input type="text" id="proj-search" name="q" size="18" value="" />
          <input type="submit" value="Search" />
        </div>
      </form>
      <div id="metanav" class="nav">
    <ul>
      <li class="first"><a href="/fipy/login">Login</a></li><li><a href="/fipy/wiki/TracGuide">Help/Guide</a></li><li><a href="/fipy/about">About Trac</a></li><li><a href="http://matforge.org">Matforge Home</a></li><li><a href="/fipy/register">Register</a></li><li><a href="http://matforge.org/participate.html">Participate</a></li><li class="last"><a href="/fipy/prefs">Preferences</a></li>
    </ul>
  </div>
    </div>
    <div id="mainnav" class="nav">
    <ul>
      <li class="first"><a href="/fipy/wiki">Wiki</a></li><li><a href="/fipy/blog">Blog</a></li><li><a href="/fipy/timeline">Timeline</a></li><li><a href="/fipy/roadmap">Roadmap</a></li><li><a href="/fipy/browser">Browse Source</a></li><li><a href="/fipy/report">View Tickets</a></li><li><a href="http://build.cmi.kent.edu:8010/waterfall">Buildbot</a></li><li class="last"><a href="http://build.cmi.kent.edu/codespeed">Codespeed</a></li>
    </ul>
  </div>
    <div id="main">
      <div id="ctxtnav" class="nav">
        <h2>Context Navigation</h2>
        <ul>
          <li class="last first"><a href="/fipy/ticket/161">Back to Ticket #161</a></li>
        </ul>
        <hr />
      </div>
    <div id="content" class="attachment">
        <h1><a href="/fipy/ticket/161">Ticket #161</a>: model3.py</h1>
        <table id="info" summary="Description">
          <tbody>
            <tr>
              <th scope="col">File model3.py,
                <span title="2742 bytes">2.7 KB</span>
                (added by wd15, <a class="timeline" href="/fipy/timeline?from=2008-11-19T10%3A11%3A56-05%3A00&amp;precision=second" title="See timeline at 11/19/08 10:11:56">6 years ago</a>)</th>
            </tr>
            <tr>
              <td class="message searchable">
                
              </td>
            </tr>
          </tbody>
        </table>
        <div id="preview" class="searchable">
          
  <table class="code"><thead><tr><th class="lineno" title="Line numbers">Line</th><th class="content"> </th></tr></thead><tbody><tr><th id="L1"><a href="#L1">1</a></th><td><span class="kn">from</span> <span class="nn">fipy</span> <span class="kn">import</span> <span class="o">*</span></td></tr><tr><th id="L2"><a href="#L2">2</a></th><td><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> time</td></tr><tr><th id="L3"><a href="#L3">3</a></th><td></td></tr><tr><th id="L4"><a href="#L4">4</a></th><td>startTime<span class="o">=</span>time<span class="p">()</span></td></tr><tr><th id="L5"><a href="#L5">5</a></th><td></td></tr><tr><th id="L6"><a href="#L6">6</a></th><td>nx<span class="o">=</span><span class="mi">41</span></td></tr><tr><th id="L7"><a href="#L7">7</a></th><td>ny<span class="o">=</span><span class="mi">3</span></td></tr><tr><th id="L8"><a href="#L8">8</a></th><td>nz<span class="o">=</span><span class="mi">14</span></td></tr><tr><th id="L9"><a href="#L9">9</a></th><td></td></tr><tr><th id="L10"><a href="#L10">10</a></th><td>dx<span class="o">=</span><span class="p">[</span><span class="mf">0.0675</span><span class="o">*</span><span class="mf">1.3</span><span class="o">**</span><span class="nb">abs</span><span class="p">(</span>i<span class="o">-</span><span class="mi">17</span><span class="p">)</span> <span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span>nx<span class="p">)]</span></td></tr><tr><th id="L11"><a href="#L11">11</a></th><td>dy<span class="o">=</span><span class="p">[</span><span class="mf">0.0675</span><span class="o">*</span><span class="mf">1.3</span><span class="o">**</span><span class="nb">abs</span><span class="p">(</span>i<span class="o">-</span><span class="p">(</span>ny<span class="o">-</span><span class="mi">1</span><span class="p">)</span><span class="o">/</span><span class="mf">2.</span><span class="p">)</span> <span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span>ny<span class="p">)]</span></td></tr><tr><th id="L12"><a href="#L12">12</a></th><td>dz<span class="o">=</span><span class="p">[</span><span class="mf">0.5</span> <span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span>nz<span class="p">)]</span></td></tr><tr><th id="L13"><a href="#L13">13</a></th><td></td></tr><tr><th id="L14"><a href="#L14">14</a></th><td>mesh<span class="o">=</span>Grid3D<span class="p">(</span>dx<span class="o">=</span>dx<span class="p">,</span>dy<span class="o">=</span>dy<span class="p">,</span>dz<span class="o">=</span>dz<span class="p">,</span>nx<span class="o">=</span>nx<span class="p">,</span>ny<span class="o">=</span>ny<span class="p">,</span>nz<span class="o">=</span>nz<span class="p">)</span></td></tr><tr><th id="L15"><a href="#L15">15</a></th><td></td></tr><tr><th id="L16"><a href="#L16">16</a></th><td>X<span class="p">,</span>Y<span class="p">,</span>Z<span class="o">=</span>mesh<span class="o">.</span>getFaceCenters<span class="p">()</span></td></tr><tr><th id="L17"><a href="#L17">17</a></th><td></td></tr><tr><th id="L18"><a href="#L18">18</a></th><td>BCs <span class="o">=</span> <span class="p">(</span>FixedValue<span class="p">(</span>mesh<span class="o">.</span>getExteriorFaces<span class="p">()</span><span class="o">&amp;</span><span class="p">(</span>X<span class="o">==</span><span class="mi">0</span><span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>Z<span class="o">&lt;</span><span class="mf">5.6</span><span class="p">),</span><span class="mf">5.6</span><span class="p">),</span></td></tr><tr><th id="L19"><a href="#L19">19</a></th><td>       FixedValue<span class="p">(</span>mesh<span class="o">.</span>getExteriorFaces<span class="p">()</span><span class="o">&amp;</span><span class="p">(</span>X<span class="o">==</span><span class="nb">max</span><span class="p">(</span>X<span class="p">))</span><span class="o">&amp;</span><span class="p">(</span>Z<span class="o">&lt;</span><span class="mf">2.9</span><span class="p">),</span><span class="mf">2.9</span><span class="p">))</span></td></tr><tr><th id="L20"><a href="#L20">20</a></th><td></td></tr><tr><th id="L21"><a href="#L21">21</a></th><td>top<span class="o">=</span>CellVariable<span class="p">(</span>name<span class="o">=</span><span class="s">'top of cell'</span><span class="p">,</span>mesh<span class="o">=</span>mesh<span class="p">,</span></td></tr><tr><th id="L22"><a href="#L22">22</a></th><td>                 value<span class="o">=</span>Z<span class="p">[</span>mesh<span class="o">.</span>_getCellFaceIDs<span class="p">()</span><span class="o">.</span>data<span class="p">[</span><span class="mi">5</span><span class="p">]])</span></td></tr><tr><th id="L23"><a href="#L23">23</a></th><td></td></tr><tr><th id="L24"><a href="#L24">24</a></th><td>bot<span class="o">=</span>CellVariable<span class="p">(</span>name<span class="o">=</span><span class="s">'bottom of cell'</span><span class="p">,</span>mesh<span class="o">=</span>mesh<span class="p">,</span></td></tr><tr><th id="L25"><a href="#L25">25</a></th><td>                 value<span class="o">=</span>Z<span class="p">[</span>mesh<span class="o">.</span>_getCellFaceIDs<span class="p">()</span><span class="o">.</span>data<span class="p">[</span><span class="mi">4</span><span class="p">]])</span></td></tr><tr><th id="L26"><a href="#L26">26</a></th><td></td></tr><tr><th id="L27"><a href="#L27">27</a></th><td>X<span class="p">,</span>Y<span class="p">,</span>Z<span class="o">=</span>mesh<span class="o">.</span>getCellCenters<span class="p">()</span></td></tr><tr><th id="L28"><a href="#L28">28</a></th><td>head<span class="o">=</span>CellVariable<span class="p">(</span>name<span class="o">=</span><span class="s">'head'</span><span class="p">,</span>mesh<span class="o">=</span>mesh<span class="p">,</span>value<span class="o">=</span><span class="mf">8.</span><span class="p">,</span>hasOld<span class="o">=</span><span class="mi">1</span><span class="p">)</span></td></tr><tr><th id="L29"><a href="#L29">29</a></th><td></td></tr><tr><th id="L30"><a href="#L30">30</a></th><td><span class="sd">'''</span></td></tr><tr><th id="L31"><a href="#L31">31</a></th><td><span class="sd">These terms control teh desaturation of a cell, slowly decreasing</span></td></tr><tr><th id="L32"><a href="#L32">32</a></th><td><span class="sd">the permeability in the x and y directions as the cell dewaters.</span></td></tr><tr><th id="L33"><a href="#L33">33</a></th><td><span class="sd">permeability in the z direction is increased as the cell dewaters</span></td></tr><tr><th id="L34"><a href="#L34">34</a></th><td><span class="sd">to allow sorce/sink terms in the top layer to continue to influence</span></td></tr><tr><th id="L35"><a href="#L35">35</a></th><td><span class="sd">the saturated zone.</span></td></tr><tr><th id="L36"><a href="#L36">36</a></th><td><span class="sd">'''</span></td></tr><tr><th id="L37"><a href="#L37">37</a></th><td></td></tr><tr><th id="L38"><a href="#L38">38</a></th><td><span class="c">###need to add this to satState variable </span></td></tr><tr><th id="L39"><a href="#L39">39</a></th><td><span class="c">#minDesat=-3. ## need to specify minimum satState or will get overflow</span></td></tr><tr><th id="L40"><a href="#L40">40</a></th><td></td></tr><tr><th id="L41"><a href="#L41">41</a></th><td>residThick<span class="o">=</span><span class="mf">1.e-2</span></td></tr><tr><th id="L42"><a href="#L42">42</a></th><td>f<span class="o">=</span><span class="mf">6.0</span></td></tr><tr><th id="L43"><a href="#L43">43</a></th><td>g<span class="o">=</span><span class="mf">1.</span><span class="o">/</span>residThick<span class="o">-</span>f</td></tr><tr><th id="L44"><a href="#L44">44</a></th><td>satState<span class="o">=</span><span class="p">(</span>head<span class="o">&lt;</span>top<span class="p">)</span><span class="o">*</span><span class="p">(</span>head<span class="o">-</span>bot<span class="p">)</span><span class="o">/</span><span class="p">(</span>top<span class="o">-</span>bot<span class="p">)</span><span class="o">+</span><span class="p">(</span>head<span class="o">&gt;</span>top<span class="p">)</span></td></tr><tr><th id="L45"><a href="#L45">45</a></th><td>cellSatH<span class="o">=</span><span class="p">((</span>satState<span class="o">&gt;=</span><span class="mi">0</span><span class="p">)</span><span class="o">*</span><span class="p">(</span>satState<span class="o">+</span>residThick<span class="o">*</span>exp<span class="p">(</span><span class="o">-</span>g<span class="o">*</span>satState<span class="p">))</span><span class="o">+</span></td></tr><tr><th id="L46"><a href="#L46">46</a></th><td>          <span class="p">(</span>satState<span class="o">&lt;</span><span class="mi">0</span><span class="p">)</span><span class="o">*</span> residThick<span class="o">*</span>exp<span class="p">(</span>f<span class="o">*</span>satState<span class="p">))</span></td></tr><tr><th id="L47"><a href="#L47">47</a></th><td>cellSatV<span class="o">=</span><span class="p">(</span>satState<span class="o">&gt;=.</span><span class="mo">01</span><span class="p">)</span><span class="o">/</span><span class="p">(</span>satState<span class="p">)</span><span class="o">+</span> <span class="p">(</span>satState<span class="o">&lt;.</span><span class="mo">01</span><span class="p">)</span><span class="o">*</span><span class="mi">100</span></td></tr><tr><th id="L48"><a href="#L48">48</a></th><td></td></tr><tr><th id="L49"><a href="#L49">49</a></th><td>spStore<span class="o">=</span><span class="mf">1.e-3</span></td></tr><tr><th id="L50"><a href="#L50">50</a></th><td>spYield<span class="o">=.</span><span class="mi">2</span></td></tr><tr><th id="L51"><a href="#L51">51</a></th><td>desat<span class="o">=</span><span class="mf">1.e-8</span></td></tr><tr><th id="L52"><a href="#L52">52</a></th><td></td></tr><tr><th id="L53"><a href="#L53">53</a></th><td>storage<span class="o">=</span>desat<span class="o">+</span><span class="p">(</span>head<span class="o">&gt;=</span>top<span class="p">)</span><span class="o">*</span>spStore<span class="o">+</span><span class="p">((</span>head<span class="o">&gt;</span>bot<span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>head<span class="o">&lt;</span>top<span class="p">))</span><span class="o">*</span>spYield</td></tr><tr><th id="L54"><a href="#L54">54</a></th><td></td></tr><tr><th id="L55"><a href="#L55">55</a></th><td>kond<span class="o">=</span>CellVariable<span class="p">(</span>name<span class="o">=</span><span class="s">'hyd.cond.'</span><span class="p">,</span>mesh<span class="o">=</span>mesh<span class="p">,</span>rank<span class="o">=</span><span class="mi">1</span><span class="p">,</span>value<span class="o">=</span><span class="mf">1.e-5</span><span class="p">)</span></td></tr><tr><th id="L56"><a href="#L56">56</a></th><td></td></tr><tr><th id="L57"><a href="#L57">57</a></th><td><span class="k">print</span> <span class="s">'a'</span><span class="p">,</span>time<span class="p">()</span><span class="o">-</span>startTime</td></tr><tr><th id="L58"><a href="#L58">58</a></th><td></td></tr><tr><th id="L59"><a href="#L59">59</a></th><td><span class="c">###second method</span></td></tr><tr><th id="L60"><a href="#L60">60</a></th><td><span class="c">#cellSat=kond*[cellSatH,cellSatH,cellSatV]</span></td></tr><tr><th id="L61"><a href="#L61">61</a></th><td></td></tr><tr><th id="L62"><a href="#L62">62</a></th><td><span class="k">print</span> <span class="s">'b'</span><span class="p">,</span>time<span class="p">()</span><span class="o">-</span>startTime</td></tr><tr><th id="L63"><a href="#L63">63</a></th><td></td></tr><tr><th id="L64"><a href="#L64">64</a></th><td><span class="c">###recharge across top of model</span></td></tr><tr><th id="L65"><a href="#L65">65</a></th><td>rech<span class="o">=</span>CellVariable<span class="p">(</span>name<span class="o">=</span><span class="s">'recharge'</span><span class="p">,</span>mesh<span class="o">=</span>mesh<span class="p">,</span></td></tr><tr><th id="L66"><a href="#L66">66</a></th><td>                  value<span class="o">=</span>where<span class="p">(</span>Z<span class="o">==</span>Z<span class="o">.</span>max<span class="p">(),</span><span class="mf">1.e-8</span><span class="p">,</span><span class="mi">0</span><span class="p">))</span></td></tr><tr><th id="L67"><a href="#L67">67</a></th><td></td></tr><tr><th id="L68"><a href="#L68">68</a></th><td><span class="k">print</span> <span class="s">'c'</span><span class="p">,</span>time<span class="p">()</span><span class="o">-</span>startTime</td></tr><tr><th id="L69"><a href="#L69">69</a></th><td></td></tr><tr><th id="L70"><a href="#L70">70</a></th><td><span class="c">###second method</span></td></tr><tr><th id="L71"><a href="#L71">71</a></th><td><span class="c">#GwEqInj=TransientTerm(coeff=storage)==DiffusionTerm(coeff=cellSat)+rech</span></td></tr><tr><th id="L72"><a href="#L72">72</a></th><td>GwEqInj<span class="o">=</span>TransientTerm<span class="p">(</span>coeff<span class="o">=</span>storage<span class="p">)</span><span class="o">==</span>DiffusionTerm<span class="p">(</span>coeff<span class="o">=</span>kond<span class="o">*</span>cellSatH<span class="o">+</span>cellSatV<span class="o">*</span>kond<span class="o">*</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">,</span><span class="mi">1</span><span class="p">])</span><span class="o">+</span>rech</td></tr><tr><th id="L73"><a href="#L73">73</a></th><td><span class="k">print</span> <span class="s">'d'</span><span class="p">,</span>time<span class="p">()</span><span class="o">-</span>startTime</td></tr><tr><th id="L74"><a href="#L74">74</a></th><td></td></tr><tr><th id="L75"><a href="#L75">75</a></th><td></td></tr><tr><th id="L76"><a href="#L76">76</a></th><td>solver <span class="o">=</span> LinearLUSolver<span class="p">(</span>tolerance<span class="o">=</span><span class="mf">1.0e-10</span><span class="p">,</span> iterations<span class="o">=</span><span class="mi">1000</span><span class="p">)</span></td></tr><tr><th id="L77"><a href="#L77">77</a></th><td></td></tr><tr><th id="L78"><a href="#L78">78</a></th><td>delT<span class="o">=</span><span class="mf">1.e7</span></td></tr><tr><th id="L79"><a href="#L79">79</a></th><td><span class="k">for</span> i <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">2</span><span class="p">):</span></td></tr><tr><th id="L80"><a href="#L80">80</a></th><td>    resid<span class="o">=</span><span class="mf">1.</span></td></tr><tr><th id="L81"><a href="#L81">81</a></th><td>    <span class="k">print</span> <span class="s">'****************'</span></td></tr><tr><th id="L82"><a href="#L82">82</a></th><td>    <span class="k">while</span> resid<span class="o">&gt;</span><span class="mf">1.e-3</span><span class="p">:</span></td></tr><tr><th id="L83"><a href="#L83">83</a></th><td>        head<span class="o">.</span>updateOld<span class="p">()</span></td></tr><tr><th id="L84"><a href="#L84">84</a></th><td>        </td></tr><tr><th id="L85"><a href="#L85">85</a></th><td>        <span class="k">print</span> satState<span class="p">()[</span>where<span class="p">((</span>X<span class="o">&lt;</span><span class="mf">25.1</span><span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>X<span class="o">&gt;</span><span class="mi">25</span><span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>Y<span class="o">&gt;.</span><span class="mi">12</span><span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>Y<span class="o">&lt;.</span><span class="mi">13</span><span class="p">))]</span></td></tr><tr><th id="L86"><a href="#L86">86</a></th><td>        <span class="k">print</span> cellSatH<span class="p">()[</span>where<span class="p">((</span>X<span class="o">&lt;</span><span class="mf">25.1</span><span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>X<span class="o">&gt;</span><span class="mi">25</span><span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>Y<span class="o">&gt;.</span><span class="mi">12</span><span class="p">)</span><span class="o">&amp;</span><span class="p">(</span>Y<span class="o">&lt;.</span><span class="mi">13</span><span class="p">))]</span></td></tr><tr><th id="L87"><a href="#L87">87</a></th><td>        resid<span class="o">=</span>GwEqInj<span class="o">.</span>sweep<span class="p">(</span>var<span class="o">=</span>head<span class="p">,</span></td></tr><tr><th id="L88"><a href="#L88">88</a></th><td>                            solver<span class="o">=</span>solver<span class="p">,</span></td></tr><tr><th id="L89"><a href="#L89">89</a></th><td>                            dt<span class="o">=</span>delT<span class="p">,</span></td></tr><tr><th id="L90"><a href="#L90">90</a></th><td>                            underRelaxation<span class="o">=</span><span class="bp">None</span><span class="p">,</span></td></tr><tr><th id="L91"><a href="#L91">91</a></th><td>                            boundaryConditions<span class="o">=</span>BCs </td></tr><tr><th id="L92"><a href="#L92">92</a></th><td>                            <span class="p">)</span></td></tr><tr><th id="L93"><a href="#L93">93</a></th><td>        <span class="k">print</span> resid</td></tr><tr><th id="L94"><a href="#L94">94</a></th><td></td></tr></tbody></table>

        </div>
    </div>
    <div id="altlinks">
      <h3>Download in other formats:</h3>
      <ul>
        <li class="last first">
          <a rel="nofollow" href="/fipy/raw-attachment/ticket/161/model3.py">Original Format</a>
        </li>
      </ul>
    </div>
    </div>
    <div id="footer" lang="en" xml:lang="en">
            <div id="projfooter"><!-- Project specific footer start -->
                <script type="text/javascript"> if (window.runOnloadHook) runOnloadHook();</script>
                <script type="text/javascript">
                    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
                    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
                </script>
                <script type="text/javascript">
                    var pageTracker = _gat._getTracker("UA-2981268-9");
                    pageTracker._initData();
                    pageTracker._trackPageview();
                </script>
            </div><!-- Project specific footer end -->
            <div id="footer_banner">
                <img src="/trac_1.0_htdocs//footer.gif" width="840" height="45" border="0" usemap="#footer" />
                <map name="footer" id="footer">
                    <area shape="rect" coords="2,3,133,42" href="http://www.kent.edu" target="_blank" alt="Kent State University" />
                    <area shape="rect" coords="137,3,240,41" href="http://www.nist.gov" target="_blank" alt="NIST" />
                    <area shape="rect" coords="244,3,372,39" href="http://www.mit.edu" target="_blank" alt="MIT" />
                    <area shape="rect" coords="376,5,606,41" href="http://www.umich.edu" target="_blank" alt="University of Michigan" />
                    <area shape="rect" coords="613,5,715,38" href="http://www.purdue.edu" target="_blank" alt="Purdue" />
                    <area shape="rect" coords="718,4,833,41" href="http://www.iastate.edu" target="_blank" alt="Iowa State University" />
                </map>
            </div>
            <br />
            <div id="altlinks">
                <br />
                <ul>
                    <li><a href="http://matdl.org/repository/about.htm" class="last first"> About </a></li>
                    <li><a href="http://matdl.org/repository/tou.htm" class="last first"> Terms of Use </a></li>
                    <li><a href="http://matdl.org/repository/contact.htm" class="last first"> Contact </a></li>
                    <li><a href="http://matdl.org/repository/priv.htm" class="last first"> Privacy Policy </a></li>
                </ul>
            </div>
	    <div id="tracfooter" lang="en" xml:lang="en">
	    <a id="tracpowered" href="http://trac.edgewall.org/"><img src="/fipy/chrome/common/trac_logo_mini.png" height="30" width="107" alt="Trac Powered" /></a>
	    <p class="left">
	    Powered by <a href="/fipy/about"><strong>Trac 1.0</strong></a><br />
	    By <a href="http://www.edgewall.org/">Edgewall Software</a>.
	    </p>
	    <p class="right">Visit the Trac open source project at<br /><a href="http://trac.edgewall.org/">http://trac.edgewall.org/</a></p>
	    </div>
        </div>
    </body>
</html>