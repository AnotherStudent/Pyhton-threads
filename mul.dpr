program mul;

{$APPTYPE CONSOLE}

{$R *.res}

uses
  System.SysUtils,
  System.Generics.Collections,
  System.Diagnostics,
  System.Classes;

function GenMatrix(const N: Integer): TArray<TArray<Double>>;
begin
  SetLength(Result, N, N);
  for var y := 0 to N - 1 do
    for var x := 0 to N - 1 do
      Result[y, x] := Random(1000);
end;

function SimpleMul(const matA, matB: TArray<TArray<Double>>): TArray<TArray<Double>>;
begin
  SetLength(Result, Length(matA), Length(matA));
  for var i := 0 to High(matA) do
    for var j := 0 to High(matB[0]) do
    begin
      var cell: Double := 0;
      for var k := 0 to High(matB) do
        cell := cell + matA[i, k] * matB[k, j];
      Result[i, j] := cell;
    end;
end;

type
  TResultThread = class(TThread)
  private
  FProc: TProc;
  public
  Result: TArray<Double>;
  constructor Create(const AProc: TProc); overload;
  procedure Execute; override;
  end;

constructor TResultThread.Create(const AProc: TProc);
begin
  inherited Create(True);
  FProc := AProc;
end;

procedure TResultThread.Execute;
begin
  FProc();
end;

function mulLineProc(const matA, matB: TArray<TArray<Double>>; i: Integer): TProc;
begin
  result :=
  procedure
  begin
    var Result: TArray<Double>;
    SetLength(Result, Length(matB[0]));

    for var j := 0 to High(matB[0]) do
    begin
      var cell: Double := 0;
      for var k := 0 to High(matB) do
        cell := cell + matA[i, k] * matB[k, j];
      Result[j] := cell;
    end;

    TResultThread(TThread.CurrentThread).Result := Result;
  end;
end;

function ThreadMul(const matA, matB: TArray<TArray<Double>>): TArray<TArray<Double>>;
begin
  SetLength(Result, 0, 0);

  var threads: TArray<TThread> := [];

  for var i := 0 to High(matA) do
  begin
    // ограничим кол-во потоков TThread.ProcessorCount
    while True do
    begin
      var count: Integer := 0;
      for var th in threads do
        if not th.Finished then
          count := count + 1;
      if count < TThread.ProcessorCount then
        break;
      sleep(0);
    end;

    var thread: TResultThread := TResultThread.Create(
      mulLineProc(matA, matB, i)
    );

    threads := threads + [thread];
    thread.FreeOnTerminate := False;
    thread.Start;
  end;

  //wait to all thread is done
  for var i in threads do
  begin
    i.WaitFor;
    Result := Result + [TResultThread(i).Result];
    i.Free;
  end;
end;

procedure Work;
begin
  var test_n: TArray<Integer> := [10, 50, 100, 200, 400, 450, 600, 800, 1500];

  for var i in test_n do
  begin
    writeln;
    writeln('mat size = (' + i.ToString + ', ' + i.ToString + ')');

    var matA: TArray<TArray<Double>> := genMatrix(i);
    var matB: TArray<TArray<Double>> := genMatrix(i);

    // simple mul
    var st1: TStopwatch := TStopwatch.StartNew;
    var matRes1: TArray<TArray<Double>> := SimpleMul(matA, matB);
    st1.Stop;
    writeln('simple matrix multiply duration: ' + st1.ElapsedMilliseconds.ToString + 'ms');

    // thread mul
    var st2: TStopwatch := TStopwatch.StartNew;
    var matRes2: TArray<TArray<Double>> := ThreadMul(matA, matB);
    st2.Stop;
    writeln('thread matrix multiply duration: ' + st2.ElapsedMilliseconds.ToString + 'ms');

    if st1.ElapsedMilliseconds > st2.ElapsedMilliseconds then
      writeln('*** Thread-driven multuply is winner! ***');


    for var y := 0 to High(matA) do
      for var x := 0 to High(matA) do
      begin
        assert(matRes1[y, x] = matRes2[y, x]);
      end;

  end;
end;

begin
  try
    Work;
  except
    on E: Exception do
      Writeln(E.ClassName, ': ', E.Message);
  end;
  readln;
end.
